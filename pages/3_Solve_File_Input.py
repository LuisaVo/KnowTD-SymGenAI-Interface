"""
Page 2C – Exercise Solver (YAML input)
Upload a YAML file containing the exercise definition, then let the engine compute
the missing variables.
"""

import streamlit as st
from streamlit_agraph import agraph, Config

# ── connect your backend here ─────────────────────────────────────────────────
from utils.bridge import cyto_to_graphviz, cyto_to_agraph, filter_cyto_elements
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

st.set_page_config(page_title="Solve – YAML | KnowTD", page_icon="✏️", layout="wide")

st.title("✏️ Solve Exercise – YAML Input")
st.caption(
    "Upload a YAML file that defines a thermodynamics exercise, including known values and the target variable. "
    "The reasoning engine will calculate the missing ones."
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
    .yaml-flow-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 0.6rem;
        margin: 0.5rem 0 0.75rem 0;
    }
    .yaml-flow-step {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 0.85rem;
        border: 1px solid #eceff4;
    }
    .yaml-flow-step strong {
        display: block;
        margin-bottom: 0.2rem;
    }
    .yaml-flow-step span {
        color: #616161;
        font-size: 0.84rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown("### Workflow")
st.caption("Upload, review, and solve in three quick steps. Results include values, equations, and reasoning graphs.")
st.markdown(
    """
    <div class="yaml-flow-grid">
        <div class="yaml-flow-step"><strong>1. Upload</strong><span>Select a YAML file with the exercise definition.</span></div>
        <div class="yaml-flow-step"><strong>2. Solve</strong><span>Inspect the uploaded content before solving.</span></div>
        <div class="yaml-flow-step"><strong>3. Inspect</strong><span>Compute targets and inspect path, graph, and equations.</span></div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# ── Step 1: Scenario / concept selection ──────────────────────────────────────
st.subheader("Step 1 – Upload a YAML file")

uploaded_file = st.file_uploader(
    "Choose a YAML file with the exercise definition",
    type=["yaml", "yml"],
    help="The YAML file should follow the specified format, including known variables and the target variable.",
)

file_content = None
if uploaded_file is not None:
    st.subheader("Step 2 – File Content & Solution")
    file_content = uploaded_file.getvalue().decode("utf-8")
else:
    st.subheader("Step 2 – File Content & Solution")

st.divider()

# ── Solve ─────────────────────────────────────────────────────────────────────
if st.button("Solve", type="primary", use_container_width=True):
    if uploaded_file is not None and not solver.load_problem(uploaded_file.getvalue().decode("utf-8")):
        st.error("Failed to load the problem. Please check the file format and contents.")
    else:
        with st.spinner("Running reasoning engine …"):
            result = solver.solve()

        if result["status"] == "success":
            st.success("Solution found!")
            
            # Two-column layout: YAML on left, results on right
            left_col, right_col = st.columns([1, 1.2])
            
            with left_col:
                st.markdown("#### YAML File")
                st.code(file_content, language="yaml")
            
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
                        show_variables = toggle_cols[0].toggle("Variables", value=True, key="file_rsn_show_variables")
                        show_equations = toggle_cols[1].toggle("Equations", value=True, key="file_rsn_show_equations")
                        show_rules = toggle_cols[2].toggle("Rules", value=True, key="file_rsn_show_rules")

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
