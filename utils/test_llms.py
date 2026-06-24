"""Batch evaluation for text-to-YAML parsing and KnowTD solving.

Usage examples:
  python utils/test_llms.py --model mistral-large-2512
  python utils/test_llms.py --model gpt-5.4 --api-key "$OPENAI_API_KEY"
  python utils/test_llms.py --models mistral-small-2603 --save-parsed out/parsed --csv-report out/report.csv
  python utils/test_llms.py --models mistral-small-2603 --save-parsed out/parsed --json-report out/report.json --csv-report out/report.csv
  python utils/test_llms.py --models mistral-large-2512 --save-parsed out/parsed --json-report out/report-mistral-large.json --csv-report out/report-mistral-large.csv
  python utils/test_llms.py --models mistral-large-2512,mistral-medium-3-5,mistral-small-2603,gpt-5.4,gpt-5.4-mini,gpt-5.5 --save-parsed out/parsed --json-report out/report-all.json --csv-report out/report-all.csv 
  
Continue after interruption:
  python utils/test_llms.py --models mistral-small-2603 --save-parsed out/parsed --json-report out/report.json --csv-report out/report.csv --resume

Restart from a specific case:
  python utils/test_llms.py --models mistral-small-2603 --save-parsed out/parsed --json-report out/report.json --csv-report out/report.csv --start-from-case Problem7

  

The script reads 13 natural-language sample problems from:
  knowtd/SampleProblems/DescriptionSampleProblems.md
It then:
1) parses each text with the selected LLM model,
2) solves the parsed structure via KnowTD,
3) compares required variable values with expected reference values.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

# Keep imports local to project root execution style.
sys.path.insert(0, os.path.abspath("."))

from utils.bridge import chat_call, validate_credentials
from utils.knowTD_solver import Solver


# Default reference values copied from knowtd/test/test_sampleProblems.py for Problem1..Problem13.
DEFAULT_EXPECTED_SOLUTIONS: dict[str, dict[str, float]] = {
	"Problem1": {"w_12": 89515.15},
	"Problem2": {"w_12": -66226.15, "del_s_12": 283.03, "q_12": 149714.13},
	"Problem3": {"q_12": -72551.64},
	"Problem4": {"q_12": 84439.32},
	"Problem5": {"q_12": 315117.85, "w_12": -70000.0},
	"Problem6": {"Q_12": -220.70},
	"Problem7": {"c_vm_Gas": 55.52},
	"Problem8": {"M_Gas": 0.03, "c_vm_Gas": 71.40},
	"Problem9": {"w_12": 44519.05},
	"Problem10": {"T_2": 345.73},
	"Problem11": {"m_I": 0.05},
	"Problem12": {"del_s_12": 15.42, "w_12": -73548.95},
	"Problem13": {"w_12": -40699.41},
}


@dataclass
class Case:
	name: str
	text: str
	expected: dict[str, float]


def parse_cases(markdown_path: Path, expected_solutions: dict[str, dict[str, float]]) -> list[Case]:
	content = markdown_path.read_text(encoding="utf-8")
	parts = re.split(r"^##\s+(Problem\d+)\s*$", content, flags=re.MULTILINE)

	# split returns [prefix, name1, body1, name2, body2, ...]
	cases: list[Case] = []
	for i in range(1, len(parts), 2):
		name = parts[i].strip()
		body = parts[i + 1].strip()
		if name not in expected_solutions:
			continue
		cases.append(Case(name=name, text=body, expected=expected_solutions[name]))

	# Keep deterministic order by problem number.
	cases.sort(key=lambda c: int(c.name.replace("Problem", "")))
	return cases


def select_api_key(model: str, explicit_api_key: str | None) -> str:
	if explicit_api_key:
		return explicit_api_key.strip()
	if "mistral" in model.lower():
		return os.environ.get("MISTRAL_API_KEY", "").strip()
	if "gpt" in model.lower() or "openai" in model.lower():
		return os.environ.get("OPENAI_API_KEY", "").strip()
	if "gemini" in model.lower():
		return os.environ.get("GOOGLE_API_KEY", "").strip()
	return ""


def to_float(value: Any) -> float:
	if isinstance(value, (int, float)):
		return float(value)
	return float(str(value).strip())


def evaluate_case(
	case: Case,
	model: str,
	api_key: str,
	solver: Solver,
	rel_tol: float,
	abs_tol: float,
	save_parsed_dir: Path | None,
) -> dict[str, Any]:
	try:
		parsed = chat_call(case.text, api_key=api_key, model=model)

		if save_parsed_dir is not None:
			save_parsed_dir.mkdir(parents=True, exist_ok=True)
			out_file = save_parsed_dir / f"{model}_{case.name}.json"
			out_file.write_text(json.dumps(parsed, indent=2), encoding="utf-8")

		solver.load_problem(parsed)
		result = solver.solve()

		if result.get("status") != "success":
			return {
				"case": case.name,
				"pass": False,
				"reason": "solver_failed",
				"details": "KnowTD returned failure status.",
				"required_parse_ok": False,
				"expected_required": sorted(case.expected.keys()),
				"parsed_required": (
					sorted(parsed.get("required_variables", [])) if isinstance(parsed, dict) else []
				),
				"checks": [],
			}

		required = result.get("required", {})
		checks: list[dict[str, Any]] = []
		all_pass = True

		for var_name, expected_val in case.expected.items():
			if var_name not in required:
				checks.append(
					{
						"variable": var_name,
						"pass": False,
						"expected": expected_val,
						"actual": None,
						"reason": "missing_required_variable",
					}
				)
				all_pass = False
				continue

			actual_val = round(to_float(required[var_name]), 2)
			close = math.isclose(actual_val, expected_val, rel_tol=rel_tol, abs_tol=abs_tol)
			checks.append(
				{
					"variable": var_name,
					"pass": close,
					"expected": expected_val,
					"actual": actual_val,
					"abs_error": abs(actual_val - expected_val),
				}
			)
			all_pass = all_pass and close

		parsed_required = set(parsed.get("required_variables", [])) if isinstance(parsed, dict) else set()
		expected_required = set(case.expected.keys())
		required_parse_ok = expected_required.issubset(parsed_required)
		if not required_parse_ok:
			all_pass = False

		return {
			"case": case.name,
			"pass": all_pass,
			"reason": "ok" if all_pass else "value_or_required_mismatch",
			"required_parse_ok": required_parse_ok,
			"expected_required": sorted(expected_required),
			"parsed_required": sorted(parsed_required),
			"checks": checks,
		}
	except Exception as exc:
		return {
			"case": case.name,
			"pass": False,
			"reason": "exception",
			"details": f"{type(exc).__name__}: {exc}",
			"required_parse_ok": False,
			"expected_required": sorted(case.expected.keys()),
			"parsed_required": [],
			"checks": [],
		}


def _build_summary(results: list[dict[str, Any]]) -> dict[str, int]:
	passed = sum(1 for r in results if r.get("pass"))
	failed = len(results) - passed
	return {"total": len(results), "passed": passed, "failed": failed}


def run_for_model(
	model: str,
	api_key: str,
	cases: list[Case],
	ontology_file: str,
	rel_tol: float,
	abs_tol: float,
	save_parsed_dir: Path | None,
	existing_results: list[dict[str, Any]] | None = None,
	on_case_completed: Callable[[dict[str, Any]], None] | None = None,
) -> dict[str, Any]:
	is_valid, validation_message = validate_credentials(api_key=api_key, model=model)
	if not is_valid:
		return {
			"model": model,
			"pass": False,
			"error": f"Credential validation failed: {validation_message}",
			"results": [],
			"summary": {"total": len(cases), "passed": 0, "failed": len(cases)},
		}

	solver = Solver(ontology_file=ontology_file)
	existing_by_case = {
		str(item.get("case")): item
		for item in (existing_results or [])
		if isinstance(item, dict) and item.get("case")
	}

	results: list[dict[str, Any]] = []
	for case in cases:
		if case.name in existing_by_case:
			results.append(existing_by_case[case.name])
			continue

		item = evaluate_case(
			case=case,
			model=model,
			api_key=api_key,
			solver=solver,
			rel_tol=rel_tol,
			abs_tol=abs_tol,
			save_parsed_dir=save_parsed_dir,
		)
		results.append(item)

		if on_case_completed is not None:
			on_case_completed(
				{
					"model": model,
					"pass": _build_summary(results)["failed"] == 0,
					"results": results,
					"summary": _build_summary(results),
				}
			)

	summary = _build_summary(results)
	return {
		"model": model,
		"pass": summary["failed"] == 0,
		"results": results,
		"summary": summary,
	}


def print_summary(report: dict[str, Any]) -> None:
	print(f"\n=== Model: {report['model']} ===")
	if report.get("error"):
		print(f"ERROR: {report['error']}")
		return

	summary = report["summary"]
	print(
		f"Total: {summary['total']} | Passed: {summary['passed']} | Failed: {summary['failed']}"
	)

	for item in report["results"]:
		status = "PASS" if item["pass"] else "FAIL"
		print(f"- {item['case']}: {status}")
		if not item["pass"]:
			print(f"  reason: {item.get('reason', 'unknown')}")
			if not item.get("required_parse_ok", True):
				print(
					"  required_variables mismatch "
					f"(expected subset={item.get('expected_required')}, "
					f"parsed={item.get('parsed_required')})"
				)
			for chk in item.get("checks", []):
				if not chk.get("pass"):
					print(
						f"  {chk.get('variable')}: expected={chk.get('expected')} "
						f"actual={chk.get('actual')} reason={chk.get('reason', 'value_mismatch')}"
					)


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		description="Evaluate text-to-YAML parsing and KnowTD solving on 13 sample problems."
	)
	parser.add_argument("--model", type=str, help="Single model name (e.g. mistral-large-2512)")
	parser.add_argument(
		"--models",
		type=str,
		help="Comma-separated model names (e.g. mistral-large-2512,gpt-5.4)",
	)
	parser.add_argument("--api-key", type=str, default=None, help="Optional API key override")
	parser.add_argument(
		"--problem-text-file",
		type=Path,
		default=Path("knowtd/SampleProblems/DescriptionSampleProblems.md"),
		help="Markdown file containing Problem1..Problem13 sections",
	)
	parser.add_argument(
		"--expected-file",
		type=Path,
		default=None,
		help=(
			"Optional JSON file with expected values map, e.g. "
			'{"Problem1": {"w_12": 89515.15}, ...}'
		),
	)
	parser.add_argument(
		"--ontology-file",
		type=str,
		default="knowtd/Ontology/thermodynamics_ontology.yaml",
		help="Path to ontology YAML used by KnowTD solver",
	)
	parser.add_argument("--rel-tol", type=float, default=1e-3, help="Relative tolerance")
	parser.add_argument("--abs-tol", type=float, default=1e-2, help="Absolute tolerance")
	parser.add_argument(
		"--save-parsed",
		type=Path,
		default=None,
		help="Optional output directory to persist parsed YAML/JSON per case",
	)
	parser.add_argument(
		"--json-report",
		type=Path,
		default=None,
		help="Optional path to write full machine-readable report JSON",
	)
	parser.add_argument(
		"--csv-report",
		type=Path,
		default=None,
		help=(
			"Optional path to write flat CSV report "
			"(one row per variable check, plus summary rows)."
		),
	)
	parser.add_argument(
		"--resume",
		action="store_true",
		help="Resume from existing --json-report by skipping already completed cases per model",
	)
	parser.add_argument(
		"--start-from-case",
		type=str,
		default=None,
		help="Optional case name to start from (e.g. Problem7)",
	)
	return parser.parse_args()


def _to_csv_rows(report: dict[str, Any]) -> list[dict[str, Any]]:
	rows: list[dict[str, Any]] = []
	model = report.get("model")

	if report.get("error"):
		rows.append(
			{
				"model": model,
				"case": "__MODEL_ERROR__",
				"case_pass": False,
				"reason": report.get("error"),
				"required_parse_ok": "",
				"variable": "",
				"variable_pass": "",
				"expected": "",
				"actual": "",
				"abs_error": "",
			}
		)
		return rows

	for item in report.get("results", []):
		case_name = item.get("case")
		case_pass = item.get("pass")
		reason = item.get("reason", "")
		required_parse_ok = item.get("required_parse_ok", "")
		checks = item.get("checks", [])

		if checks:
			for chk in checks:
				rows.append(
					{
						"model": model,
						"case": case_name,
						"case_pass": case_pass,
						"reason": reason,
						"required_parse_ok": required_parse_ok,
						"variable": chk.get("variable"),
						"variable_pass": chk.get("pass", False),
						"expected": chk.get("expected", ""),
						"actual": chk.get("actual", ""),
						"abs_error": chk.get("abs_error", ""),
					}
				)
		else:
			rows.append(
				{
					"model": model,
					"case": case_name,
					"case_pass": case_pass,
					"reason": reason,
					"required_parse_ok": required_parse_ok,
					"variable": "",
					"variable_pass": "",
					"expected": "",
					"actual": "",
					"abs_error": "",
				}
			)

	summary = report.get("summary", {})
	rows.append(
		{
			"model": model,
			"case": "__SUMMARY__",
			"case_pass": report.get("pass", False),
			"reason": (
				f"total={summary.get('total', 0)};"
				f"passed={summary.get('passed', 0)};"
				f"failed={summary.get('failed', 0)}"
			),
			"required_parse_ok": "",
			"variable": "",
			"variable_pass": "",
			"expected": "",
			"actual": "",
			"abs_error": "",
		}
	)
	return rows


def write_csv_report(reports: list[dict[str, Any]], csv_path: Path) -> None:
	csv_path.parent.mkdir(parents=True, exist_ok=True)

	fieldnames = [
		"model",
		"case",
		"case_pass",
		"reason",
		"required_parse_ok",
		"variable",
		"variable_pass",
		"expected",
		"actual",
		"abs_error",
	]

	rows: list[dict[str, Any]] = []
	for report in reports:
		rows.extend(_to_csv_rows(report))

	with csv_path.open("w", newline="", encoding="utf-8") as f:
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerows(rows)


def write_reports_checkpoint(
	reports: list[dict[str, Any]],
	json_report: Path | None,
	csv_report: Path | None,
) -> None:
	if json_report is not None:
		json_report.parent.mkdir(parents=True, exist_ok=True)
		json_report.write_text(json.dumps(reports, indent=2), encoding="utf-8")
	if csv_report is not None:
		write_csv_report(reports, csv_report)


def load_existing_reports(json_report: Path) -> list[dict[str, Any]]:
	if not json_report.exists():
		return []
	try:
		data = json.loads(json_report.read_text(encoding="utf-8"))
		if isinstance(data, list):
			return [d for d in data if isinstance(d, dict)]
	except Exception:
		pass
	return []


def main() -> int:
	args = parse_args()

	models: list[str] = []
	if args.model:
		models.append(args.model.strip())
	if args.models:
		models.extend([m.strip() for m in args.models.split(",") if m.strip()])
	if not models:
		print("Provide --model or --models.")
		return 2

	expected_solutions: dict[str, dict[str, float]] = DEFAULT_EXPECTED_SOLUTIONS
	if args.expected_file is not None:
		if not args.expected_file.exists():
			print(f"Expected values file not found: {args.expected_file}")
			return 2
		expected_raw = json.loads(args.expected_file.read_text(encoding="utf-8"))
		expected_solutions = {
			str(problem): {str(var): float(value) for var, value in values.items()}
			for problem, values in expected_raw.items()
		}

	if not args.problem_text_file.exists():
		print(f"Problem text file not found: {args.problem_text_file}")
		return 2

	cases = parse_cases(args.problem_text_file, expected_solutions)
	if len(cases) != 13:
		print(
			f"Expected 13 cases from markdown, found {len(cases)}. "
			"Check section headers (## Problem1 ... ## Problem13)."
		)
		return 2

	if args.start_from_case:
		matching_case_index = next(
			(i for i, c in enumerate(cases) if c.name == args.start_from_case),
			None,
		)
		if matching_case_index is None:
			print(f"Case not found for --start-from-case: {args.start_from_case}")
			return 2
		cases = cases[matching_case_index:]

	if args.resume and args.json_report is None:
		print("--resume requires --json-report so completed cases can be loaded.")
		return 2

	existing_reports_by_model: dict[str, dict[str, Any]] = {}
	if args.resume and args.json_report is not None:
		for report in load_existing_reports(args.json_report):
			model_name = report.get("model")
			if isinstance(model_name, str) and model_name:
				existing_reports_by_model[model_name] = report

	reports_by_model: dict[str, dict[str, Any]] = {}
	for model in models:
		api_key = select_api_key(model, args.api_key)
		if not api_key:
			reports_by_model[model] = {
				"model": model,
				"pass": False,
				"error": (
					"Missing API key. Provide --api-key or set env var "
					"MISTRAL_API_KEY / OPENAI_API_KEY depending on model."
				),
				"results": [],
				"summary": {"total": len(cases), "passed": 0, "failed": len(cases)},
			}
			continue

		existing_results = existing_reports_by_model.get(model, {}).get("results", [])

		def _on_case_completed(partial_report: dict[str, Any]) -> None:
			reports_by_model[model] = partial_report
			ordered_reports = [reports_by_model[m] for m in models if m in reports_by_model]
			write_reports_checkpoint(ordered_reports, args.json_report, args.csv_report)
			print(
				f"Checkpoint saved after {model} / "
				f"{partial_report['summary']['total']} case(s)."
			)

		report = run_for_model(
			model=model,
			api_key=api_key,
			cases=cases,
			ontology_file=args.ontology_file,
			rel_tol=args.rel_tol,
			abs_tol=args.abs_tol,
			save_parsed_dir=args.save_parsed,
			existing_results=existing_results,
			on_case_completed=_on_case_completed,
		)
		reports_by_model[model] = report
		ordered_reports = [reports_by_model[m] for m in models if m in reports_by_model]
		write_reports_checkpoint(ordered_reports, args.json_report, args.csv_report)

	reports = [reports_by_model[m] for m in models if m in reports_by_model]
	for report in reports:
		print_summary(report)

	if args.json_report is not None:
		print(f"\nWrote report: {args.json_report}")
	if args.csv_report is not None:
		print(f"Wrote CSV report: {args.csv_report}")

	overall_pass = all(r.get("pass", False) for r in reports)
	return 0 if overall_pass else 1


if __name__ == "__main__":
	raise SystemExit(main())
