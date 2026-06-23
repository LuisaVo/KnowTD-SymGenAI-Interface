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
            tab_vals, tab_eq, tab_sol, tab_rsn = st.tabs(
                ["Computed Values", "Used Equations", "Solution Path", "Reasoning Path"]
            )

            with tab_vals:
                st.markdown("#### Required variables")
                req = result.get("required", {})
                # for sym, val in req.items():
                #     formatted_val = f"{val:.4g}" if isinstance(val, (int, float)) else str(val)
                #     st.metric(label=sym, value=formatted_val)
                r_cols = st.columns(min(len(req), 4))
                for i, (sym, val) in enumerate(req.items()):
                    with r_cols[i % 4]:
                        st.markdown(f"**${sym}$** = ${val}$" if val else "—")

                intermediate = result.get("intermediate", {})
                with st.expander("Intermediate variables", expanded=False):
                    if intermediate:
                        o_cols = st.columns(3)
                        for i, (sym, val) in enumerate(intermediate.items()):
                            with o_cols[i % 3]:
                                st.markdown(f"**${sym}$**  =  ${val}$" if val else f"**${sym}$**")
                        # for sym, val in intermediate.items():
                        #     formatted_val = f"{val:.4g}" if isinstance(val, (int, float)) else str(val)
                        #     st.metric(label=sym, value=formatted_val)
                    else:
                        st.caption("No intermediate variables available.")

            with tab_eq:
                st.markdown("#### Equations used")
                for eq, ex in result["equations_used"].items():
                    st.text(eq)
                    st.code(ex, language="math")

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

        else:
            st.error("The engine could not find a solution. Check your inputs.")
