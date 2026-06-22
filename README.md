# KnowTD Interface
KnowTD is a Streamlit interface for exploring a thermodynamics ontology and solving thermodynamics exercises with a knowledge-based reasoning engine.

## What The Interface Is For

Use KnowTD when you want to:

- understand ontology concepts, variables, equations, and rule constraints,
- solve exercises from plain text, a structured form, or a YAML file,
- inspect the solution path and reasoning graph,
- generate scenario-based YAML exercises.

## Interface Pages And Use Cases

The app is organized in the sidebar into the following pages.

### 1) Ontology (`pages/1_Ontology.py`)

Use this page when you need to inspect the domain model itself.

- Browse concepts with descriptions and related elements.
- Browse variables with symbol, unit, and default value.
- Browse equations with required concepts and rule constraints.
- Open an interactive ontology graph with toggles for concepts, variables, equations, and rules.

Best for:

- onboarding new users,
- checking variable naming and units,
- understanding why a specific equation/rule is used during solving.

### 2) Solve From Text (`pages/2_Solve_Text_Input.py`)

Use this page when the exercise is given as natural language.

- Choose a model and provide an API key.
- Paste exercise text.
- Parse text to structured problem data.
- Review and edit extracted content if needed.
- Run KnowTD solver and inspect computed values and used equations.

Best for:

- fast prototyping from textbook-style prompts,
- classroom/demo workflows,
- converting free-text tasks into structured input quickly.

### 3) Solve From Form (`pages/3_Solve_Form_Input.py`)

Use this page when you want full control over structured input.

- Load a sample problem or create a custom problem class.
- Set editable attributes.
- Enter known variable values.
- Select required variables explicitly.
- Solve and inspect values, solution path, and reasoning graph.

Best for:

- controlled experiments,
- debugging solver behavior,
- reproducible, step-by-step exercise setup.

### 4) Solve From File (`pages/4_Solve_File_Input.py`)

Use this page when you already have a YAML exercise definition.

- Upload YAML file.
- Preview file content.
- Solve and inspect computed values and equations.

Best for:

- batch/authoring pipelines that already output YAML,
- regression checks on known problem files,
- collaboration with shared exercise files.

### 5) Scenarios (`pages/5_Scenarios.py`)

Use this page to browse predefined scenario combinations and generate exercises.

- Filter scenario table by ID, heat/work behavior, and attributes.
- View template YAML or exercise YAML.
- Generate scenario-specific exercises.
- Download generated YAML and inspect generated solution path details.

Best for:

- systematic scenario exploration,
- exercise authoring,
- creating new test cases quickly.

## Typical Workflows

### Workflow A: Solve A Textbook Problem Quickly

1. Open Solve From Text.
2. Paste the problem statement.
3. Parse and review extracted structure.
4. Solve and inspect required/intermediate values.

### Workflow B: Debug A Specific Assumption

1. Open Solve From Form.
2. Select the problem class and set process attributes.
3. Fill only known variables.
4. Select required targets and solve.
5. Inspect reasoning graph to understand dependency chain.

### Workflow C: Work From Existing Files

1. Open Solve From File.
2. Upload YAML.
3. Solve and verify output.

### Workflow D: Generate New Exercises

1. Open Scenarios.
2. Filter/select scenario.
3. Generate exercise YAML.
4. Download and optionally validate with Solve From File.

## Project Structure

```text
Interface/
├── Overview.py
├── pages/
│   ├── 1_Ontology.py
│   ├── 2_Solve_Text_Input.py
│   ├── 3_Solve_Form_Input.py
│   ├── 4_Solve_File_Input.py
│   └── 5_Scenarios.py
├── utils/
│   ├── bridge.py
│   └── knowTD_solver.py
└── requirements.txt
```

## Requirements

- Python 3.9+
- macOS/Linux/Windows

## Installation

From the project root (`Interface/`):

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate         # Windows (PowerShell)
pip install -r requirements.txt
```

## Run The App

```bash
streamlit run Overview.py
```

Then open the local URL shown in the terminal (typically `http://localhost:8501`).
