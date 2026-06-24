"""
Page 2A – Exercise Solver (Natural language input)
Paste or type a thermodynamics exercise in plain text. The tool parses the
exercise, extracts known values, and computes the missing ones.
"""

import streamlit as st
import os
import yaml
import re
from pathlib import Path
from streamlit_agraph import agraph, Config
from streamlit_ace import st_ace, THEMES
from utils.sidebar_navigation import render_sidebar_navigation

# ── connect your backend here ─────────────────────────────────────────────────
from utils.bridge import (
    chat_call,
    validate_credentials,
    cyto_to_graphviz,
    cyto_to_agraph,
    filter_cyto_elements,
)
from utils.knowTD_solver import Solver
solver = Solver(ontology_file="knowtd/Ontology/thermodynamics_ontology.yaml")
# ──────────────────────────────────────────────────────────────────────────────

GRAPH_COLORS = {
    "required": "indianred1",
    "assignment": "palegreen1",
    "variable": "white",
    "equation": "silver",
    "rule": "steelblue2",
}

st.set_page_config(page_title="Solve – NL | KnowTD", page_icon="assets/Logo2.svg", layout="wide")

render_sidebar_navigation()

st.title(":material/chat: Solve Exercise – Natural Language Input")
st.markdown("### Workflow")
st.caption("Use this page from left to right: set up model access, provide the problem text, review extracted YAML, and solve.")
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
    .nl-process-flow {
        display: flex;
        align-items: center;
        justify-content: space-around;
        margin: 1rem 0 0.25rem 0;
        flex-wrap: wrap;
        gap: 0.5rem;
    }
    .nl-flow-step {
        display: flex;
        flex-direction: column;
        justify-content: top;
        align-items: center;
        text-align: center;
        padding: 0.9rem;
        background: #f8f9fa;
        border-radius: 8px;
        min-width: 150px;
        min-height: 110px;
        font-size: 0.9rem;
    }
    .nl-flow-step strong {
        margin-bottom: 0.25rem;
    }
    .nl-flow-step div {
        font-size: 0.8rem;
        color: #666;
        line-height: 1.3;
    }
    .nl-flow-arrow {
        font-size: 1.3rem;
        color: #999;
    }
    </style>
    <div class="nl-process-flow">
        <div class="nl-flow-step">
            <strong>1. API Setup</strong>
            <div>Select model and<br>enter API key</div>
        </div>
        <div class="nl-flow-arrow">→</div>
        <div class="nl-flow-step">
            <strong>2. Exercise Text</strong>
            <div>Type or paste your problem<br>or load a<br>sample exercise</div>
        </div>
        <div class="nl-flow-arrow">→</div>
        <div class="nl-flow-step">
            <strong>3. YAML Extraction</strong>
            <div>Let the LLM convert<br>your text to<br>structured YAML</div>
        </div>
        <div class="nl-flow-arrow">→</div>
        <div class="nl-flow-step">
            <strong>4. Review</strong>
            <div>Confirm or edit<br>parsed values</div>
        </div>
        <div class="nl-flow-arrow">→</div>
        <div class="nl-flow-step">
            <strong>5. Solve</strong>
            <div>Get values, solution path,<br>reasoning graph, and equations</div>
        </div>
        <div class="nl-flow-arrow">→</div>
        <div class="nl-flow-step">
            <strong>6. Inspect</strong>
            <div>Inspect the solution path<br>to gain insights into how<br>the solution was obtained.</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# ── API Setup text input ───────────────────────────────────────────────────────
st.subheader("1 API setup")
st.caption("Please enter your API Key for the desired model. You can use OpenAI or Mistral.")

model_options = [
    # "mistral-large-latest",
    "mistral-large-2512",
    "mistral-medium-3-5",
    "mistral-small-2603",
    # "mistral-medium-latest",
    # "mistral-small-latest",
    "gpt-5.5",
    "gpt-5.4",
    "gpt-5.4-mini",
    # "gemini-3.5-flash",
    # "gemini-3.1-flash-lite",
]

if "llm_model" not in st.session_state:
    st.session_state["llm_model"] = model_options[0]
    
if "mistral" in st.session_state["llm_model"] and "llm_api_key" not in st.session_state:
    st.session_state["llm_api_key"] = os.environ.get("MISTRAL_API_KEY", "")
elif "gpt" in st.session_state["llm_model"] and st.session_state["llm_api_key"] == os.environ.get("MISTRAL_API_KEY", ""):
    st.session_state["llm_api_key"] = os.environ.get("OPENAI_API_KEY", "")


model_col, api_col, info_col = st.columns([1,2,1])
with api_col:
    st.text_input(
        "LLM API key",
        key="llm_api_key",
        type="password",
        placeholder="Enter your API key",
        help="Used for parsing the exercise text with the selected LLM model.",
    )
with model_col:
    st.selectbox(
        "Model",
        options=model_options,
        key="llm_model",
        help="Choose the model used for natural language parsing.",
    )
with info_col:
    st.info("""
**:material/admin_panel_settings: Security Note**

Your API key is stored only in your browser's session and is not saved on our servers. You will need to re-enter it if you refresh the page or close your browser.
""")

if not st.session_state["llm_api_key"].strip():
    st.warning("Enter an API key to enable parsing.", icon=":material/key:")

st.divider()

# ── Exercise text input ───────────────────────────────────────────────────────
st.subheader("2 Enter the exercise")
st.markdown("Type or paste your thermodynamics exercise in plain text or choose a sample exercise (right).")
tab_input, tab_tip = st.columns([2,1])

with tab_input:
    example_text = (
        "Enter your text here or choose a sample exercise"
    )

    example_exercise = """A gas in a cylinder is compressed reversibly from v_1 = 0.05 m^3/kg to v_2 = 0.02 m^3/kg. The initial temperature is T_1 = 298 K. The process is adiabatic. What is the work supplied per kilogram of gas?
    The gas is ideal, with R = 287 J/(kg K) and c_v = 1010 J/(kg K). The required variable is w_12, the process is isentropic."""

    if "exercise_text" not in st.session_state:
        st.session_state["exercise_text"] = ""

    if "parsed_yaml" not in st.session_state:
        st.session_state["parsed_yaml"] = ""

    if "parsed_yaml_edit" not in st.session_state:
        st.session_state["parsed_yaml_edit"] = ""


    EXAMPLE_FILE = Path("utils/DescriptionSampleProblems.md")


    def load_examples_from_markdown(markdown_path: Path) -> dict[str, str]:
        """Parse markdown sections in the form '## ProblemX' into label->text map."""
        if not markdown_path.exists():
            return {}

        content = markdown_path.read_text(encoding="utf-8")
        parts = re.split(r"^##\s+(Problem\d+)\s*$", content, flags=re.MULTILINE)
        examples: dict[str, str] = {}
        for i in range(1, len(parts), 2):
            name = parts[i].strip()
            body = parts[i + 1].strip()
            if body:
                examples[name] = body
        return examples


    markdown_examples = load_examples_from_markdown(EXAMPLE_FILE)
    example_labels = sorted(markdown_examples.keys(), key=lambda x: int(x.replace("Problem", "")))

    if "selected_example_label" not in st.session_state:
        st.session_state["selected_example_label"] = example_labels[0] if example_labels else ""


    def load_selected_example_text() -> None:
        label = st.session_state.get("selected_example_label", "")
        if label and label in markdown_examples:
            st.session_state["exercise_text"] = markdown_examples[label]
        else:
            st.session_state["exercise_text"] = example_exercise

    col_hint, col_select, col_ex = st.columns([2, 2, 1], vertical_alignment='bottom')
    # with col_select:
    #     st.selectbox(
    #         "Example",
    #         options=example_labels if example_labels else ["Fallback example"],
    #         key="selected_example_label",
    #         help="Select one of the sample problems from utils/DescriptionSampleProblems.md",
    #     )
    # with col_ex:
    #     st.button("Load example", width='stretch', on_click=load_selected_example_text)

    if not markdown_examples:
        st.caption("Could not read utils/DescriptionSampleProblems.md, using fallback inline example.")

    exercise_text = st.text_area(
        "Exercise text",
        key="exercise_text",
        placeholder=example_text,
        height="stretch",
        help="Paste the full exercise text here, including all given values and the question.",
    )

with tab_tip:
    # design_services
    st.info("""**Quick Tips:**
            
**:material/design_services: Units Matter**

Always use SI units (Kelvin, Joules, Pascal, etc.). If your problem uses other units, convert first or specify in the text.

**:material/folder_open: Try an Example**

You can choose from several sample exercises to test the system and get familiar with the workflow.
    """)
    col_select_example, col_load = st.columns([2,1], vertical_alignment="bottom")
    with col_select_example:
        st.selectbox(
                "Example",
                options=example_labels if example_labels else ["Fallback example"],
                key="selected_example_label",
                help="Select one of the sample problems from utils/DescriptionSampleProblems.md",
            )
    with col_load:
        st.button("Load example", width='stretch', on_click=load_selected_example_text)

st.divider()

# ── Parse & Solve ─────────────────────────────────────────────────────────────
if st.button(
    "Convert to YAML",
    type="primary",
    width='stretch',
    disabled=not exercise_text.strip() or not st.session_state["llm_api_key"].strip(),
):
    with st.spinner("Validating API key …"):
        is_valid_key, validation_message = validate_credentials(
            api_key=st.session_state["llm_api_key"].strip(),
            model=st.session_state["llm_model"],
        )

    if not is_valid_key:
        st.error("Please enter a valid API key (or choose an accessible model) and try again.")
        st.info(validation_message)
    else:
        with st.spinner("Parsing exercise text …"):
            parsed_yaml = chat_call(
                exercise_text,
                api_key=st.session_state["llm_api_key"].strip(),
                model=st.session_state["llm_model"],
            )
        st.session_state["parsed_yaml"] = parsed_yaml
        st.session_state["parsed_yaml_edit"] = yaml.dump(parsed_yaml, default_flow_style=False, indent=4)

if st.session_state["parsed_yaml"]:
    parsed_yaml = st.session_state["parsed_yaml"]

    st.success("Exercise parsed successfully.")

    confirm_col, parse_col = st.columns([2, 3])

    with parse_col:
        st.markdown("#### Extracted information")
        new = st_ace(
    value=st.session_state["parsed_yaml_edit"],
    language="yaml",
    theme="tomorrow",
    keybinding="vscode",
    height=800,
    font_size=14,
    tab_size=2,
    show_gutter=True,
    wrap=True,
    auto_update=True,
)
        if st.button(
            "Update", type="primary", disabled=new is None or new.strip(". ") == ""
        ):
            st.session_state["parsed_yaml"] = new
            parsed_yaml = new

    with confirm_col:
        st.markdown("#### Confirm or correct the parsed values")
        st.info("""Inspect the YAML file on the right and adjust it before solving.""", icon=":material/info:")    
        st.markdown("""
#### Common pitfalls: 

**:material/add: Incorrect Signs:** 

When work or heat are removed, the LLMs often use the incorrect sign. Check Variables `Q`, `W`, `q` and `w`.

**:material/design_services: Unit conversions:** 

LLMs often introduce conversion mistakes if other units than the SI units were given.

**:material/compare_arrows: Variable mixups:** 

LLMs often mix up similar variables such as `c_v` and `c_vm` (molar heat capacity). Especially specific and molar variables are mixed up.
""")

        # corrected = {}
        # for sym, val in parsed["known_values"].items():
        #     corrected[sym] = st.number_input(f"{sym}", value=float(val), key=f"nl_{sym}", format="%.6g")

        # target_override = st.text_input(
        #     "Target variable symbol",
        #     value=parsed["target_variable"],
        #     key="nl_target",
        #)

    st.divider()

    if st.button("Solve with extracted values", type="primary"):        
        with st.spinner("Running reasoning engine …"):
            solver.load_problem(st.session_state["parsed_yaml"])
            result = solver.solve()

        if result["status"] == "success":
            st.success("Solution found!")
            
            # Two-column layout: edited YAML on left, results on right
            left_col, right_col = st.columns([1, 1.2])
            
            with left_col:
                st.markdown("#### Edited YAML")
                st.code(st.session_state["parsed_yaml_edit"], language="yaml")
            
            with right_col:
                st.markdown("#### Solution")
                
                # Required variables at the top
                st.markdown("**Required variables:**")
                req = result.get("required", {})
                r_cols = st.columns(min(len(req), 4))
                for i, (sym, val) in enumerate(req.items()):
                    with r_cols[i % 4]:
                        st.markdown(f"**${sym}$** = ${val}$" if val else "—")
                
                # Intermediate variables in expander
                intermediate = result.get("intermediate", {})
                with st.expander("Intermediate variables", expanded=False):
                    if intermediate:
                        o_cols = st.columns(3)
                        for i, (sym, val) in enumerate(intermediate.items()):
                            with o_cols[i % 3]:
                                st.markdown(f"**${sym}$**  =  ${val}$" if val else f"**${sym}$**")
                    else:
                        st.caption("No intermediate variables available.")
                
                st.markdown("")
                
                # Tabs for graphs and equations
                tab_sol, tab_rsn, tab_eq = st.tabs(
                    ["Solution Path", "Reasoning Graph", "Used Equations"]
                )

                with tab_sol:
                    graph_solution = result.get("graph_solution", result.get("nodes+edges", []))
                    if graph_solution:
                        st.graphviz_chart(cyto_to_graphviz(graph_solution, GRAPH_COLORS))
                    else:
                        st.info("No solution path available.")

                with tab_rsn:
                    graph_reasoning = result.get("graph_reasoning", result.get("nodes+edges", []))
                    if graph_reasoning:
                        st.caption("Interactive graph: drag nodes, zoom, and pan.")
                        toggle_cols = st.columns(3)
                        show_variables = toggle_cols[0].toggle("Variables", value=True, key="txt_rsn_show_variables")
                        show_equations = toggle_cols[1].toggle("Equations", value=True, key="txt_rsn_show_equations")
                        show_rules = toggle_cols[2].toggle("Rules", value=True, key="txt_rsn_show_rules")

                        filtered_graph = filter_cyto_elements(
                            graph_reasoning,
                            show_variables=show_variables,
                            show_equations=show_equations,
                            show_rules=show_rules,
                        )

                        if not filtered_graph:
                            st.info("No graph elements match the selected filters.")
                        else:
                            nodes, edges = cyto_to_agraph(filtered_graph)
                            config = Config(
                                width=650,
                                height=600,
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

                with tab_eq:
                    st.markdown("#### Used Equations")
                    for eq, ex in result["equations_used"].items():
                        st.text(eq)
                        st.code(ex, language="math")

        else:
            st.error("The engine could not find a solution. Check your inputs.")