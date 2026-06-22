"""
Page 2C – Exercise Solver (YAML input)
Upload a YAML file containing the exercise definition, then let the engine compute
the missing variables.
"""

import streamlit as st
import graphviz

# ── connect your backend here ─────────────────────────────────────────────────
from utils.knowTD_solver import Solver
solver = Solver(ontology_file="knowtd/Ontology/thermodynamics_ontology.yaml")
# ──────────────────────────────────────────────────────────────────────────────

st.set_page_config(page_title="Solve – YAML | KnowTD", page_icon="✏️", layout="wide")

st.title("✏️ Solve Exercise – YAML Input")
st.caption(
    "Upload a YMAL file that defines a thermodynamics exercise, including known values and the target variable. "
    "The reasoning engine will calculate the missing ones."
)

st.divider()

# ── Step 1: Scenario / concept selection ──────────────────────────────────────
st.subheader("Step 1 – Upload a YAML file")

uploaded_file = st.file_uploader(
    "Choose a YAML file with the exercise definition",
    type=["yaml", "yml"],
    help="The YAML file should follow the specified format, including known variables and the target variable.",
)

if uploaded_file is not None:
    st.subheader("Step 2 – File Content")
    file_content = uploaded_file.getvalue().decode("utf-8")
    st.code(file_content, language="yaml")
st.divider()

# ── Solve ─────────────────────────────────────────────────────────────────────
if st.button("Solve", type="primary", width='stretch'):
    if uploaded_file is not None and not solver.load_problem(uploaded_file.getvalue().decode("utf-8")):
        st.error("Failed to load the problem. Please check the file format and contents.")
    else:
        with st.spinner("Running reasoning engine …"):
            result = solver.solve()

            # # ── Placeholder result ────────────────────────────────────────────
            # result = {
            #     "status": "success",
            #     "all": {
            #         "R": 8.314,
            #         "P": 101325,
            #     },
            #     "required": {
            #         "R": 8.314,
            #     },
            #     "intermediate": {
            #         "P": 101325,
            #     },
            #     "equations_all": {
            #         "IdealGasLaw": "PV = nRT",
            #     },
            #     "equations_used": ["PV = nRT"],
            # }
            # # ─────────────────────────────────────────────────────────────────

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
