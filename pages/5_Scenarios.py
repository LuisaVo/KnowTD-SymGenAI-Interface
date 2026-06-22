"""
Page 6 – Exercise Generation
Browse the 12 thermodynamic scenarios, filter by attributes or ID, select one
and inspect the stored YAML definition.
"""

import streamlit as st
import os
import pathlib
import yaml
from utils.bridge import gen_problem_with_values

# ── Scenario catalogue ────────────────────────────────────────────────────────

SCENARIOS = [
    {"id": "01", "Q": "Q ≠ 0", "W": "W = 0", "reversible": False, "isochoric": False, "isobaric": False, "isothermal": False, "isentropic": False, "adiabatic": False, "polytropic": False},
    {"id": "02", "Q": "Q ≠ 0", "W": "W = 0", "reversible": False, "isochoric": True,  "isobaric": False, "isothermal": False, "isentropic": False, "adiabatic": False, "polytropic": False},
    {"id": "03", "Q": "Q ≠ 0", "W": "W = 0", "reversible": True,  "isochoric": True,  "isobaric": False, "isothermal": False, "isentropic": False, "adiabatic": False, "polytropic": False},
    {"id": "04", "Q": "Q = 0", "W": "W ≠ 0", "reversible": False, "isochoric": False, "isobaric": False, "isothermal": False, "isentropic": False, "adiabatic": True,  "polytropic": False},
    {"id": "05", "Q": "Q = 0", "W": "W ≠ 0", "reversible": False, "isochoric": True,  "isobaric": False, "isothermal": False, "isentropic": False, "adiabatic": True,  "polytropic": False},
    {"id": "06", "Q": "Q = 0", "W": "W ≠ 0", "reversible": True,  "isochoric": False, "isobaric": False, "isothermal": False, "isentropic": True,  "adiabatic": True,  "polytropic": True },
    {"id": "07", "Q": "Q ≠ 0", "W": "W ≠ 0", "reversible": False, "isochoric": False, "isobaric": False, "isothermal": False, "isentropic": False, "adiabatic": False, "polytropic": False},
    {"id": "08", "Q": "Q ≠ 0", "W": "W ≠ 0", "reversible": False, "isochoric": True,  "isobaric": False, "isothermal": False, "isentropic": False, "adiabatic": False, "polytropic": False},
    {"id": "09", "Q": "Q ≠ 0", "W": "W ≠ 0", "reversible": True,  "isochoric": False, "isobaric": False, "isothermal": False, "isentropic": False, "adiabatic": False, "polytropic": False},
    {"id": "10", "Q": "Q ≠ 0", "W": "W ≠ 0", "reversible": True,  "isochoric": False, "isobaric": False, "isothermal": False, "isentropic": False, "adiabatic": False, "polytropic": True },
    {"id": "11", "Q": "Q ≠ 0", "W": "W ≠ 0", "reversible": True,  "isochoric": False, "isobaric": True,  "isothermal": False, "isentropic": False, "adiabatic": False, "polytropic": True },
    {"id": "12", "Q": "Q ≠ 0", "W": "W ≠ 0", "reversible": True,  "isochoric": False, "isobaric": False, "isothermal": True,  "isentropic": False, "adiabatic": False, "polytropic": True },
]

BOOL_PROPS = ["reversible", "isochoric", "isobaric", "isothermal", "isentropic", "adiabatic", "polytropic"]

# Maps scenario ID → YAML file path (relative to repo root)
BASE = pathlib.Path("exercise-generation/Generated Exercises")
FOLDER_MAP = {
    "01": BASE / "NoWork",
    "02": BASE / "NoWork",
    "03": BASE / "NoWork",
    "04": BASE / "NoHeat",
    "05": BASE / "NoHeat",
    "06": BASE / "NoHeat",
    "07": BASE / "HeatAndWork",
    "08": BASE / "HeatAndWork",
    "09": BASE / "HeatAndWork",
    "10": BASE / "HeatAndWork",
    "11": BASE / "HeatAndWork",
    "12": BASE / "HeatAndWork",
}


def template_yaml_path(scenario_id: str) -> pathlib.Path:
    folder = FOLDER_MAP[scenario_id]
    return folder / f"Scenario_{scenario_id}_template.yaml"


def exercise_yaml_path(scenario_id: str) -> pathlib.Path:
    folder = FOLDER_MAP[scenario_id]
    return folder / f"Scenario_{scenario_id}.yaml"


def tag(label: str, color: str) -> str:
    """Return a coloured HTML badge."""
    return (
        f'<span style="background:{color};color:#fff;padding:2px 8px;'
        f'border-radius:4px;font-size:0.78em;margin-right:4px;">{label}</span>'
    )


def scenario_tags(s: dict) -> str:
    parts = []
    if s["reversible"]:
        parts.append(tag("reversible", "#2e7d32"))
    else:
        parts.append(tag("irreversible", "#c62828"))
    for prop in ["adiabatic", "isochoric", "isobaric", "isothermal", "isentropic", "polytropic"]:
        if s[prop]:
            parts.append(tag(prop, "#1565c0"))
    return "".join(parts)


def reset_filters() -> None:
    st.session_state["f_id"] = ""
    st.session_state["f_heat"] = "any"
    st.session_state["f_work"] = "any"
    st.session_state["f_props"] = []


# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="Exercise Generation | KnowTD", page_icon="⚙️", layout="wide")

st.title("⚙️ Exercise Generation")
st.caption(
    "Browse the 12 thermodynamic scenarios. Filter by attribute or ID, then "
    "click a scenario to view its YAML definition."
)

# ── Filters ───────────────────────────────────────────────────────────────────
if "f_id" not in st.session_state:
    st.session_state["f_id"] = ""
if "f_heat" not in st.session_state:
    st.session_state["f_heat"] = "any"
if "f_work" not in st.session_state:
    st.session_state["f_work"] = "any"
if "f_props" not in st.session_state:
    st.session_state["f_props"] = []
if "selected_view" not in st.session_state:
    st.session_state["selected_view"] = "template"

# filter_header, reset_col = st.columns([6, 1])
# filter_header.subheader("Filter scenarios")
# reset_col.

# fcol1, fcol2, fcol3 = st.columns([1, 1, 2])

# with fcol1:
#     id_filter = st.text_input("Scenario ID (e.g. 01, 07)", placeholder="all", key="f_id")

# with fcol2:
#     heat_filter = st.selectbox("Heat (Q)", ["any", "heat transfer allowed", "no heat transfer allowed"], key="f_heat")
#     work_filter = st.selectbox("Work (W)", ["any", "work allowed", "no work allowed"], key="f_work")

# with fcol3:
#     prop_filter = st.multiselect(
#         "Process attributes",
#         options=["reversible", "irreversible", "adiabatic", "isochoric", "isobaric", "isothermal", "isentropic", "polytropic"],
#         key="f_props",
#     )

# ── Scenario table ────────────────────────────────────────────────────────────
st.subheader(f"Possible Scenarios")


# Session state for selected scenario
if "selected_scenario" not in st.session_state:
    st.session_state["selected_scenario"] = None

header_cols = st.columns([0.5, 2, 2, 2.5, 1, 2])
with header_cols[0]:
    st.markdown("**ID**")
    id_filter = st.text_input("", placeholder="01, 07", key="f_id")
with header_cols[1]:
    st.markdown("**Heat**")
    heat_filter = st.selectbox("", ["any", "heat transfer allowed", "no heat transfer allowed"], key="f_heat")
with header_cols[2]:
    st.markdown("**Work**")
    work_filter = st.selectbox("", ["any", "work allowed", "no work allowed"], key="f_work")
with header_cols[3]:
        st.markdown("**Process attributes**")
        prop_filter = st.multiselect(
        "",
        options=["reversible", "irreversible", "adiabatic", "isochoric", "isobaric", "isothermal", "isentropic", "polytropic"],
        key="f_props",
    )
with header_cols[4]:
    st.button("↺ Reset filters", on_click=reset_filters, use_container_width=True)
header_cols[5].markdown("")

# ── Apply filters ─────────────────────────────────────────────────────────────
filtered = SCENARIOS

if id_filter.strip():
    ids = [x.strip().zfill(2) for x in id_filter.replace(",", " ").split()]
    filtered = [s for s in filtered if s["id"] in ids]

if heat_filter == "heat transfer allowed":
    filtered = [s for s in filtered if s["Q"] == "Q ≠ 0"]
elif heat_filter == "no heat transfer allowed":
    filtered = [s for s in filtered if s["Q"] == "Q = 0"]

if work_filter == "work allowed":
    filtered = [s for s in filtered if s["W"] == "W ≠ 0"]
elif work_filter == "no work allowed":
    filtered = [s for s in filtered if s["W"] == "W = 0"]

for prop in prop_filter:
    if prop == "irreversible":
        filtered = [s for s in filtered if not s["reversible"]]
    else:
        filtered = [s for s in filtered if s[prop]]

st.divider()

# ── Scenarios‚ ─────────────────────────────────────────────────────────────
if not filtered:
    st.info("No scenarios match the current filters.")
else:

    for s in filtered:
        row = st.columns([0.5, 2, 2, 2.5, 1, 1, 1])
        row[0].markdown(f"**{s['id']}**")
        row[1].markdown(s["Q"])
        row[2].markdown(s["W"])
        row[3].markdown(scenario_tags(s), unsafe_allow_html=True)
        if row[4].button("Show Template", key=f"sel_template_{s['id']}"):
            st.session_state["selected_scenario"] = s["id"]
            st.session_state["selected_view"] = "template"
        if row[5].button("Show Exercise", key=f"sel_exercise_{s['id']}"):
            st.session_state["selected_scenario"] = s["id"]
            st.session_state["selected_view"] = "exercise"
        if row[6].button("Generate Exercise", key=f"sel_generate_{s['id']}"):
            st.session_state["selected_scenario"] = s["id"]
            st.session_state["selected_view"] = "generate"

    st.divider()

    # ── YAML viewer ───────────────────────────────────────────────────────────
    sel_id = st.session_state.get("selected_scenario")

    if sel_id is None:
        st.info("Click **Select** on a scenario above to view its YAML Template file or a generated exercise.")
    else:
        sel = next((s for s in SCENARIOS if s["id"] == sel_id), None)
        if sel is None:
            st.warning("Selected scenario not found.")
        else:
            view_mode = st.session_state.get("selected_view", "template")
            # template and exercise read from files, generate creates new data (not saved in files)
            
            if view_mode == "generate":
                st.subheader(f"Scenario {sel_id} — YAML exercise")
                attributes = {attr: val for attr,val in sel.items() if attr not in ['id', 'Q', 'W']}
                attribute_assignment = [('12', f'is_{attr}', val) if attr not in ['adiabatic', 'reversible'] else ('12', attr, val) for attr, val in attributes.items()]
                values = {}
                if sel["Q"] == "Q = 0":
                    values['Q_12'] = 0
                if sel["W"] == "W = 0":
                    values['W_12'] = 0      
                generated_problem, solution, solution_path = gen_problem_with_values('SingleStep', attributes=attribute_assignment, values=values )
                yaml_text = yaml.safe_dump(generated_problem, sort_keys=False, allow_unicode=True)
                
                file_name = f"scenario_{sel_id}.yaml"
            else:
                if view_mode == "exercise":
                    st.subheader(f"Scenario {sel_id} — YAML exercise")
                    path = exercise_yaml_path(sel_id)
                else: #template
                    st.subheader(f"Scenario {sel_id} — YAML template")
                    path = template_yaml_path(sel_id)
                    
                if path.exists():
                    yaml_text = path.read_text(encoding="utf-8")
                    file_name = path.name
                else:
                    st.error(f"YAML file not found at `{path}`.")
                    st.stop()
            
            st.markdown(scenario_tags(sel), unsafe_allow_html=True)
            st.markdown("")

            st.code(yaml_text, language="yaml")

            st.download_button(
                label="⬇ Download YAML",
                data=yaml_text,
                file_name=file_name,
                mime="text/yaml",
            )
            if view_mode == "generate":
                st.divider()
                st.success("Generated exercise with solution path.")

                res_col, steps_col = st.columns([1, 1])

                with res_col:
                    st.markdown("#### Computed values")
                    st.markdown("**Required variables:**")
                    for sym, val in solution.items():
                        st.metric(label=sym, value=str(val))

                    st.markdown("**Intermediate variables:**")
                    path_variables = solution_path.get("variables", {}) if isinstance(solution_path, dict) else {}
                    intermediate_variables = {
                        sym: val for sym, val in path_variables.items() if sym not in solution
                    }
                    if intermediate_variables:
                        for sym, val in intermediate_variables.items():
                            st.metric(label=sym, value=str(val))
                    else:
                        st.info("No intermediate variables recorded.")

                with steps_col:
                    st.markdown("#### Equations used")
                    equations = solution_path.get("equations", {}) if isinstance(solution_path, dict) else {}
                    if equations:
                        for eq_id, eq_data in equations.items():
                            if isinstance(eq_data, dict):
                                eq_name = eq_data.get("name", eq_id)
                                eq_expression = eq_data.get("expression", "")
                            else:
                                eq_name = eq_id
                                eq_expression = eq_data
                            st.text(str(eq_name))
                            st.code(str(eq_expression), language="math")
                    else:
                        st.info("No equations available for the solution path.")

