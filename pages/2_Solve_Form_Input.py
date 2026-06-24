"""
Page 3 (copy) – Exercise Solver (Form input)
Streamlit port of the Dash app in knowtd/scripts/app.py.

Flow mirrors the original Dash UI:
  1. (Optional) Load a sample problem
  2. Select a problem class  →  creates a ProblemInput object
  3. Set boolean / enum attributes  →  "Apply Attributes"
  4. Enter variable values + mark required  →  "Solve"
  5. View solution table and reasoning graph
"""

from __future__ import annotations
import os, sys
import streamlit as st
from streamlit_agraph import agraph, Config
from utils.bridge import cyto_to_graphviz, cyto_to_agraph, filter_cyto_elements, format_unit_display

# ── Path setup ────────────────────────────────────────────────────────────────
# ProblemInput and friends live in knowtd/scripts/ and use bare imports, so
# that directory must be on sys.path.  OntologyProblemInput also loads the
# ontology schema with a path relative to knowtd/, so we temporarily chdir
# there for the initial import.
_SCRIPTS = os.path.abspath("knowtd/scripts")
_KNOWTD  = os.path.abspath("knowtd")
for _p in [_SCRIPTS, _KNOWTD]:
    if _p not in sys.path:
        sys.path.insert(0, _p)


from ProblemHandler import ProblemHandler
from ProblemSolver  import ProblemSolver
from ProblemInput import (
        ProblemInput,
        Equilibrium, SingleStep, SequentialSteps, CyclicProcess,
        SampleSingleStep, SampleCyclicProcess,
    )

# _cwd = os.getcwd()
# os.chdir(_KNOWTD)
# try:
    
# finally:
#     os.chdir(_cwd)

# ProblemInput.initialize_solver uses "Ontology/…" relative to cwd.
# Patch it to use the absolute path so it works from Interface/.
_ONTOLOGY_ABS = os.path.abspath("knowtd/Ontology/thermodynamics_ontology.yaml")

def _initialize_solver_patched(self):
    self.handler = ProblemHandler(_ONTOLOGY_ABS, self.yamlInput)
    self.solver  = ProblemSolver(
        list(self.handler.instances("Variable")),
        self.handler.create_equations(),
        self.handler.problem.required_variables,
    )

ProblemInput.initialize_solver = _initialize_solver_patched

# ── Constants ─────────────────────────────────────────────────────────────────
EXAMPLE_OPTIONS: list[str] = (
    ["Custom Input"]
    + [f"Single Step {i}" for i in range(1, 14)]
    + ["Cyclic Process 1", "Cyclic Process 2"]
)

PROBLEM_CLASSES: list[str] = [
    "State in Equilibrium",
    "Single Step",
    "Sequential Steps",
    "Cyclic Process",
]

# Variables that are structural (IDs, references) – show read-only, skip value input
DISABLED_VARS: set[str] = {
    "id", "equation_of_state", "transition", "material",
    "final_state", "initial_state", "related_changes_and_states", "related_changes", "related_states"
}

# Attributes that are fixed system defaults – show as read-only checkbox
FIXED_ATTRS: set[str] = {"closed", "equilibrium", "motion", "homogeneous", "pure", "mixed"}

# Variables that should be visible but not editable by users.
READONLY_VARS: set[str] = {"T0", "W_a", "Rbar"}

GRAPH_COLORS: dict[str, str] = {
    "required":   "indianred1",
    "assignment": "palegreen1",
    "variable":   "white",
    "equation":   "silver",
    "rule":       "steelblue2",
}

# ── Helpers ───────────────────────────────────────────────────────────────────

def _make_problem_input(problem_class: str, num_states: int = 3) -> ProblemInput | None:
    mapping = {
        "State in Equilibrium": lambda: Equilibrium(),
        "Single Step":          lambda: SingleStep(),
        "Sequential Steps":     lambda: SequentialSteps(num_states),
        "Cyclic Process":       lambda: CyclicProcess(num_states),
    }
    factory = mapping.get(problem_class)
    return factory() if factory else None


def _load_sample(example: str) -> ProblemInput | None:
    if "Single Step " in example:
        return SampleSingleStep(example.replace("Single Step ", ""))
    if "Cyclic Process " in example:
        return SampleCyclicProcess(example.replace("Cyclic Process ", ""))
    return None


def _reset_state() -> None:
    for key in list(st.session_state.keys()):
        if key in {
            "pi",
            "attrs_done",
            "result",
            "example_select",
            "problem_class",
            "num_states",
            "focused_visible_fields",
            "required_variables_select",
            "entry_mode",
        } or key.startswith(("attr_", "var_", "req_")):
            del st.session_state[key]
    st.session_state["example_select"] = "Custom Input"
    st.session_state.pi = None
    st.session_state.attrs_done = False
    st.session_state.result = None


# ── Session state init ────────────────────────────────────────────────────────
for _k, _v in [("pi", None), ("attrs_done", False), ("result", None)]:
    if _k not in st.session_state:
        st.session_state[_k] = _v

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="Solve – Form | KnowTD", page_icon="✏️", layout="wide")
st.title("✏️ Solve Exercise – Form Input")
st.caption(
    "Load a sample problem or configure a custom one, "
    "enter only the known values, mark targets, then press **Solve**."
)
st.markdown(
    """
    <style>
    div.stButton > button {
        background: #343deb !important;
        color: #ffffff !important;
        border: 1px solid #343deb !important;
        border-radius: 10px;
        font-weight: 600;
    }
    div.stButton > button:hover {
        background: #2b33c7 !important;
        border-color: #2b33c7 !important;
        color: #ffffff !important;
    }
    div.stDownloadButton > button {
        background: #343deb !important;
        color: #ffffff !important;
        border: 1px solid #343deb !important;
        border-radius: 10px;
        font-weight: 600;
    }
    div.stDownloadButton > button:hover {
        background: #2b33c7 !important;
        border-color: #2b33c7 !important;
        color: #ffffff !important;
    }
    .form-flow-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
        gap: 0.6rem;
        margin: 0.5rem 0 0.75rem 0;
    }
    .form-flow-step {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 0.85rem;
        border: 1px solid #eceff4;
    }
    .form-flow-step strong {
        display: block;
        margin-bottom: 0.2rem;
    }
    .form-flow-step span {
        color: #616161;
        font-size: 0.84rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown("### Workflow")
st.caption("Follow these steps to configure a problem, enter known values, and solve with full transparency.")
st.markdown(
    """
    <div class="form-flow-grid">
        <div class="form-flow-step"><strong>1. Example</strong><span>Load a sample or keep custom input.</span></div>
        <div class="form-flow-step"><strong>2. Class</strong><span>Select the problem class and state count.</span></div>
        <div class="form-flow-step"><strong>3. Attributes</strong><span>Set process and system attributes.</span></div>
        <div class="form-flow-step"><strong>4. Values</strong><span>Enter known variables in focused mode.</span></div>
        <div class="form-flow-step"><strong>5. Targets</strong><span>Pick required variables and solve.</span></div>
        <div class="form-flow-step"><strong>6. Solve and Inspect</strong><span>Gain insights into how the solution was obtained.<\span></div>
    </div>
    """,
    unsafe_allow_html=True,
)
top_cols = st.columns([6, 1])
with top_cols[1]:
    st.button("↺ Reset", key="reset_form", on_click=_reset_state, use_container_width=True)
st.divider()

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1 – Example loader
# ═══════════════════════════════════════════════════════════════════════════════
with st.expander("1. Load an Example or select custom input", expanded=True):
    example_choice = st.selectbox(
        "Select a sample problem",
        EXAMPLE_OPTIONS,
        key="example_select",
    )

    if example_choice != "Custom Input":
        if st.button("Load example", key="btn_load"):
            try:
                pi_loaded = _load_sample(example_choice)
            except Exception as exc:
                st.error(f"Could not load sample '{example_choice}': {exc}")
            else:
                if pi_loaded is None:
                    st.error(f"No sample loader found for '{example_choice}'.")
                else:
                    _reset_state()
                    st.session_state.pi         = pi_loaded
                    st.session_state.attrs_done = True   # sample problems are pre-configured
                    st.rerun()

        # Fallback: if a sample is selected but session_state was reset, restore it.
        if st.session_state.pi is None:
            try:
                restored = _load_sample(example_choice)
            except Exception:
                restored = None
            if restored is not None:
                st.session_state.pi = restored
                st.session_state.attrs_done = True

        # Show question if a sample is already loaded and matches the selection
        pi_cur = st.session_state.pi
        if pi_cur is not None and hasattr(pi_cur, "question") and pi_cur.question:
            st.markdown("**Problem description:**")
            st.markdown(pi_cur.question)

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2 – Custom problem class
# ═══════════════════════════════════════════════════════════════════════════════
with st.expander(
    "2. Select Problem Class  (skip if you loaded an example)",
    expanded=(example_choice == "Custom Input" and st.session_state.pi is None),
):
    prob_class = st.radio("Problem class", PROBLEM_CLASSES, key="problem_class", index=1)

    num_states = 3
    if prob_class in ("Sequential Steps", "Cyclic Process"):
        num_states = st.number_input(
            "Number of states (≥ 3)", min_value=3, max_value=20, value=3, step=1,
            key="num_states",
        )

    if st.button("Create problem", key="btn_create"):
        _reset_state()
        st.session_state.pi = _make_problem_input(prob_class, int(num_states))
        st.rerun()

pi: ProblemInput | None = st.session_state.pi

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 3 – Attribute input
# ═══════════════════════════════════════════════════════════════════════════════
if pi is not None:
    with st.expander(
        "3. Set Attributes",
        expanded=(not st.session_state.attrs_done),
    ):
        any_attrs = False
        bool_attr_keys: set[str] = set()
        for concept in pi.get_concepts():
            attrs = [
                attr
                for attr in pi.get_attributes(concept)
                if attr not in FIXED_ATTRS and attr not in DISABLED_VARS
            ]
            if not attrs:
                continue
            any_attrs = True
            st.markdown(f"**{concept}**")
            n_cols = min(len(attrs), 4)
            cols   = st.columns(n_cols)
            for i, attr in enumerate(attrs):
                val = pi.get_value(concept, attr)
                key = f"attr_{concept}_{attr}"
                is_bool_attr = val in ("True", "False", "None")
                with cols[i % n_cols]:
                    if is_bool_attr:
                        bool_attr_keys.add(key)
                        st.checkbox(
                            attr,
                            value=(val == "True"),
                            key=key,
                        )
                    else:
                        st.text_input(attr, value="" if val == "None" else val, key=key)

        if not any_attrs:
            st.info("No attributes for this problem class.")

        if st.button("✅ Apply attributes", key="btn_attrs"):
            for concept in pi.get_concepts():
                for attr in pi.get_attributes(concept):
                    k = f"attr_{concept}_{attr}"
                    if k in st.session_state and attr not in FIXED_ATTRS and attr not in DISABLED_VARS:
                        raw_val = st.session_state[k]
                        if k in bool_attr_keys:
                            normalized = "True" if bool(raw_val) else "False"
                        else:
                            if isinstance(raw_val, str):
                                raw_val = raw_val.strip()
                            normalized = "None" if raw_val in (None, "", "None") else str(raw_val)
                        pi.set_value(concept, attr, normalized)
            st.session_state.attrs_done = True
            st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 4 – Variable value input
# ═══════════════════════════════════════════════════════════════════════════════
if pi is not None and st.session_state.attrs_done:
    with st.expander("4. Enter Known Variable Values", expanded=True):
        st.markdown("Use **Focused mode** to work with only the fields relevant to your question.")

        entry_mode = st.radio(
            "Input mode",
            ["Focused (recommended)", "Show all fields"],
            horizontal=True,
            key="entry_mode",
        )

        editable_fields = []
        default_visible = []
        label_by_key = {}

        for concept in pi.get_concepts():
            for var in pi.get_variables(concept):
                if var in DISABLED_VARS or var in READONLY_VARS:
                    continue
                field_key = f"{concept}::{var}"
                unit_str = pi.get_unit_of_variable(var)
                label_by_key[field_key] = f"{var} ({concept})"
                editable_fields.append((concept, var, field_key))

                raw_val = pi.get_value(concept, var)
                if raw_val != "None":
                    default_visible.append(field_key)

        if entry_mode == "Focused (recommended)":
            selected_fields = st.multiselect(
                "Visible fields",
                options=[field_key for _, _, field_key in editable_fields],
                default=default_visible,
                format_func=lambda k: label_by_key[k],
                key="focused_visible_fields",
                help="Search and select only the variables you want to edit for this task.",
            )
            visible_field_keys = set(selected_fields)
            if not visible_field_keys:
                st.info("Select a few fields above to start entering values.")
        else:
            visible_field_keys = {field_key for _, _, field_key in editable_fields}

        for concept in pi.get_concepts():
            var_list = [
                v for v in pi.get_variables(concept)
                if v not in DISABLED_VARS and v not in READONLY_VARS and f"{concept}::{v}" in visible_field_keys
            ]
            if not var_list:
                continue

            st.markdown(f"**{concept}**")
            cols = st.columns(3)
            for i, var in enumerate(var_list):
                raw_val  = pi.get_value(concept, var)
                unit_str = pi.get_unit_of_variable(var)
                unit_display = format_unit_display(unit_str)
                placeholder = "unknown"

                with cols[i % 3]:
                    input, unit = st.columns([4, 1], vertical_alignment="bottom")
                    with input:
                        st.text_input(
                            f"**{var}  ({concept})**",
                            value="" if raw_val == "None" else raw_val,
                            key=f"var_{concept}_{var}",
                            placeholder=placeholder,
                        )
                    with unit:
                        if unit_display:                            
                            st.caption(unit_display)
                            st.text(" ")
            st.markdown("")   # spacing between concepts

        st.divider()

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 5 – Required variables + solve
# ═══════════════════════════════════════════════════════════════════════════════
if pi is not None and st.session_state.attrs_done:
    with st.expander("5. Select Required Variable(s)", expanded=True):
        required_candidates = {}
        for concept in pi.get_concepts():
            for var in pi.get_variables(concept):
                if var in DISABLED_VARS or var in READONLY_VARS:
                    continue
                concept_id = pi.get_value(concept, "id")
                req_id = f"{var}_{concept_id}"
                label = f"{var} ({concept})"
                required_candidates[req_id] = {
                    "concept": concept,
                    "var": var,
                    "label": label,
                }

        preselected_required = [
            rid for rid in pi.required_variables if rid in required_candidates
        ]

        selected_required = st.multiselect(
            "Required variables to compute",
            options=list(required_candidates.keys()),
            default=preselected_required,
            format_func=lambda rid: required_candidates[rid]["label"],
            key="required_variables_select",
            help="Select one or more target variables that the solver should compute.",
        )

        st.divider()

        if st.button("Solve", type="primary", use_container_width=True):
            # ── read variable values from session_state ──
            for concept in pi.get_concepts():
                for var in pi.get_variables(concept):
                    if var in DISABLED_VARS or var in READONLY_VARS:
                        continue
                    v_key = f"var_{concept}_{var}"

                    if v_key in st.session_state:
                        v = st.session_state[v_key]
                        pi.set_value(concept, var, v if v.strip() else "None")

            # sync required variables from step 5 selection
            pi.required_variables = []
            for rid in selected_required:
                candidate = required_candidates.get(rid)
                if candidate is None:
                    continue
                try:
                    pi.add_required(candidate["concept"], candidate["var"])
                except Exception:
                    pass

            if not pi.required_variables:
                st.warning("Please mark at least one variable as **required** before solving.")
            else:
                with st.spinner("Running reasoning engine …"):
                    pi.writeYAML()
                    try:
                        pi.send_to_solver()
                        req_out, other_out = pi.get_solution_elements_required()
                        graph_sol    = pi.get_graph_elements()
                        graph_reason = pi.get_reasoning_graph_elements()
                        st.session_state.result = {
                            "status":    "success",
                            "required":  req_out,
                            "other":     other_out,
                            "graph_sol": graph_sol,
                            "graph_rsn": graph_reason,
                        }
                    except Exception as exc:
                        st.session_state.result = {"status": "error", "error": str(exc)}
                st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 6 – Solution
# ═══════════════════════════════════════════════════════════════════════════════
result = st.session_state.result
if result is not None:
    st.divider()

    if result["status"] == "error":
        st.error("KnowTD could not find a solution.")
        with st.expander("Error details"):
            st.code(result["error"])

    else:
        st.success("Solution found!")
        tab_vals, tab_sol, tab_rsn = st.tabs(
            ["Values", "Solution Path", "Reasoning Graph"]
        )

        # ── Values tab ────────────────────────────────────────────────────────
        with tab_vals:
            req   = result["required"]
            other = result["other"]

            if req:
                st.markdown("#### Required variables")
                r_cols = st.columns(min(len(req), 4))
                for i, (sym, val) in enumerate(req.items()):
                    with r_cols[i % 4]:
                        st.markdown(f"**${sym}$** = ${val}$" if val else "—")

            if other:
                with st.expander("All other solved variables"):
                    o_cols = st.columns(3)
                    for i, (sym, val) in enumerate(other.items()):
                        with o_cols[i % 3]:
                            st.markdown(f"**${sym}$**  =  ${val}$" if val else f"**${sym}$**")

        # ── Solution Path graph ───────────────────────────────────────────────
        with tab_sol:
            if result["graph_sol"]:
                st.graphviz_chart(cyto_to_graphviz(result["graph_sol"], GRAPH_COLORS))
            else:
                st.info("No solution graph available.")

        # ── Reasoning Graph ───────────────────────────────────────────────────
        with tab_rsn:
            if result["graph_rsn"]:
                st.caption("Interactive graph: drag nodes, zoom with mouse wheel/trackpad, and pan by dragging the canvas.")
                toggle_cols = st.columns(3)
                show_variables = toggle_cols[0].toggle("Variables", value=True, key="rsn_show_variables")
                show_equations = toggle_cols[1].toggle("Equations", value=True, key="rsn_show_equations")
                show_rules = toggle_cols[2].toggle("Rules", value=True, key="rsn_show_rules")

                filtered_rsn_graph = filter_cyto_elements(
                    result["graph_rsn"],
                    show_variables=show_variables,
                    show_equations=show_equations,
                    show_rules=show_rules,
                )

                if not filtered_rsn_graph:
                    st.info("No graph elements match the selected filters.")
                nodes, edges = cyto_to_agraph(filtered_rsn_graph)
                config = Config(
                    width=1300,
                    height=860,
                    directed=True,
                    physics=True,
                    hierarchical=False,
                    solver="repulsion",
                    minVelocity=0.2,
                    maxVelocity=30,
                    stabilization=True,
                    fit=True,
                    timestep=0.35,
                    interaction={
                        "dragNodes": True,
                        "dragView": True,
                        "zoomView": True,
                        "navigationButtons": True,
                        "keyboard": True,
                        "hover": True,
                    },
                )
                agraph(nodes=nodes, edges=edges, config=config)
            else:
                st.info("No reasoning graph available.")

