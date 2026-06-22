"""
Page 2A – Exercise Solver (Natural language input)
Paste or type a thermodynamics exercise in plain text. The tool parses the
exercise, extracts known values, and computes the missing ones.
"""

import streamlit as st
import os
import json
import graphviz

# ── connect your backend here ─────────────────────────────────────────────────
from utils.bridge import chat_call, validate_credentials
from utils.knowTD_solver import Solver
solver = Solver(ontology_file="knowtd/Ontology/thermodynamics_ontology.yaml")
# ──────────────────────────────────────────────────────────────────────────────

st.set_page_config(page_title="Solve – NL | KnowTD", page_icon="💬", layout="wide")

st.title("💬 Solve Exercise – Natural Language Input")
st.markdown("""1. Enter your desired model and api key.
2. Type or paste a thermodynamics exercise in plain text. 
3. The system will extract the variables you can adjust the input if desired.
4. Send the extracted values to KnowTD and view results.
Optional 5. Let a LLM explain the solution path."""
)

st.divider()

# ── API Setup text input ───────────────────────────────────────────────────────
st.subheader("1 API setup")
st.caption("Please enter your API Key for the desired model. You can use OpenAI, Mistral or Gemini.")
model_options = [
    "mistral-large-latest",
    "mistral-medium-latest",
    "mistral-small-latest",
    "gpt-5.2",
    "gpt-4",
    "gpt-5-nano"
]

if "llm_model" not in st.session_state:
    st.session_state["llm_model"] = model_options[0]
    
if "mistral" in st.session_state["llm_model"] and "llm_api_key" not in st.session_state:
    st.session_state["llm_api_key"] = os.environ.get("MISTRAL_API_KEY", "")
elif "gpt" in st.session_state["llm_model"] and st.session_state["llm_api_key"] == os.environ.get("MISTRAL_API_KEY", ""):
    st.session_state["llm_api_key"] = os.environ.get("OPENAI_API_KEY", "")


model_col, api_col = st.columns([1,2])
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

if not st.session_state["llm_api_key"].strip():
    st.warning("Enter an API key to enable parsing.", icon="🔐")

st.divider()

# ── Exercise text input ───────────────────────────────────────────────────────
st.subheader("2 Enter the exercise")

example_text = (
    "A container holds 2 moles of an ideal gas at a temperature of 300 K "
    "and a pressure of 101325 Pa. What is the volume of the gas?"
)

example_exercise = """A gas in a cylinder is compressed reversibly from v_1 = 0.05 m^3/kg to v_2 = 0.02 m^3/kg. The initial temperature is T_1 = 298 K. The process is adiabatic. What is the work supplied per kilogram of gas?
The gas is ideal, with R = 287 J/(kg K) and c_v = 1010 J/(kg K). The required variable is w_1, the process is isentropic."""

if "exercise_text" not in st.session_state:
    st.session_state["exercise_text"] = ""

if "parsed_yaml" not in st.session_state:
    st.session_state["parsed_yaml"] = ""

if "parsed_yaml_edit" not in st.session_state:
    st.session_state["parsed_yaml_edit"] = ""


def load_example_text() -> None:
    st.session_state["exercise_text"] = example_exercise

exercise_text = st.text_area(
    "Exercise text",
    key="exercise_text",
    placeholder=example_text,
    height=160,
    help="Paste the full exercise text here, including all given values and the question.",
)

col_hint, col_ex = st.columns([3, 1])
with col_ex:
    st.button("Load example", width='stretch', on_click=load_example_text)

st.divider()

# ── Parse & Solve ─────────────────────────────────────────────────────────────
if st.button(
    "Parse & Solve",
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
        st.session_state["parsed_yaml_edit"] = json.dumps(parsed_yaml, indent=4)

if st.session_state["parsed_yaml"]:
    parsed_yaml = st.session_state["parsed_yaml"]

    st.success("Exercise parsed successfully.")

    parse_col, confirm_col = st.columns([1, 1])

    with parse_col:
        st.markdown("#### Extracted information")
        # st.markdown(f"**Scenario detected:** {parsed_yaml['problem_class']}")
        # st.markdown(f"**Target variable:** **{parsed_yaml['required_variables']}**")

        new = st.text_area("Rewrite the answer", value=st.session_state["parsed_yaml_edit"], height=300, help="The YAML content extracted from the exercise text. Adjust if necessary before solving.")
        if st.button(
            "Update", type="primary", disabled=new is None or new.strip(". ") == ""
        ):
            st.session_state["parsed_yaml"] = new
            parsed_yaml = new

    with confirm_col:
        st.markdown("#### Confirm or correct the parsed values")
        st.info("If the extraction looks wrong, adjust the values before solving.", icon="ℹ️")

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

            res_col, steps_col = st.columns([1, 1])

            with res_col:
                st.markdown("#### Computed values")
                st.markdown("**Required variables:**")
                for sym, val in result["required"].items():
                    formatted_val = f"{val:.4g}" if isinstance(val, (int, float)) and val > 0 else str(val)
                    st.metric(label=sym, value=formatted_val)
                    st.markdown("**Intermediate variables:**")
                for sym, val in result["intermediate"].items():
                    formatted_val = f"{val:.4g}" if isinstance(val, (int, float)) and val > 0 else str(val)
                    st.metric(label=sym, value=formatted_val)

            with steps_col:
                st.markdown("#### Equations used")
                for eq, ex in result["equations_used"].items():
                    st.text(eq)
                    st.code(ex, language="math")
            
            graph = graphviz.Digraph()
            colors = {"required": "indianred1", "assignment": "palegreen1", "variable": "white", "equation": "silver", "rule": "steelblue2"}
            for elem in result["nodes+edges"]:
                if 'source' in elem['data'] and 'target' in elem['data']:
                    graph.edge(elem['data']['source'], elem['data']['target'], label=elem['data'].get('label', ''))
                else:
                    graph.node(elem['data']['id'], 
                               label=elem['data']['label'], 
                               shape="ellipse" if elem['data']['type'] in ["variable", "required", "assignment"] else "box",
                               fillcolor=colors.get(elem['classes'], "white"),
                               style="filled"
                               )
            st.graphviz_chart(graph)

        else:
            st.error("The engine could not find a solution. Check your inputs.")
