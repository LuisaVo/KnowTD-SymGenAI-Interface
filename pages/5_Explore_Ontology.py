"""
Page 1 – Ontology Viewer
Browse concepts, variables, and equations from the thermodynamics ontology.
"""

import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import re
from utils.sidebar_navigation import render_sidebar_navigation

# ── connect your backend here ─────────────────────────────────────────────────
from utils.bridge import Ontology
ontology = Ontology(filename="knowtd/Ontology/thermodynamics_ontology.yaml")
def list_to_nice_string(items: list[str], camel=False) -> str:
    """Convert a list of strings into a nice human-readable string."""
    if not camel:
        items = [camel_to_normal(item) for item in items]
    if not items:
        return ""
    elif len(items) == 1:
        return items[0]
    else:
        return ", ".join(items[:-1]) + " and " + items[-1]
    
def camel_to_normal(name):
    # Inserts an underscore before any capital letter that follows a lowercase letter or digit
    # Then converts the entire string to lowercase
    return re.sub( r"([A-Z])|([0-9]+)", r" \1\2", name).strip().replace('* ', '*')
st.set_page_config(page_title="Ontology | KnowTD", page_icon="assets/Logo.svg", layout="wide")
render_sidebar_navigation()

def snake_to_camel(name):
    splitted = name.split('_')
    return ''.join(word.capitalize() for word in splitted)

st.title(":material/schema: Thermodynamics Ontology")
st.caption("Browse the concepts, variables, and equations defined in the ontology.")
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
    .onto-flow-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 0.6rem;
        margin: 0.5rem 0 0.75rem 0;
    }
    .onto-flow-step {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 0.85rem;
        border: 1px solid #eceff4;
    }
    .onto-flow-step strong {
        display: block;
        margin-bottom: 0.2rem;
    }
    .onto-flow-step span {
        color: #616161;
        font-size: 0.84rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown("### Workflow")
st.caption("Explore thermodynamics knowledge from three perspectives and inspect how they connect in the graph.")
st.markdown(
    """
    <div class="onto-flow-grid">
        <div class="onto-flow-step"><strong>Concepts</strong><span>Read conceptual descriptions and relations.</span></div>
        <div class="onto-flow-step"><strong>Variables</strong><span>Inspect symbols, SI units, and defaults.</span></div>
        <div class="onto-flow-step"><strong>Equations</strong><span>Review expressions, slots, and constraints.</span></div>
        <div class="onto-flow-step"><strong>Graph</strong><span>Visualize dependencies across all layers.</span></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Tabs: one per knowledge layer ─────────────────────────────────────────────
tab_concepts, tab_variables, tab_equations, tab_graph = st.tabs(
    ["Concepts", "Variables", "Equations", "Graph view"]
)

# ── Concepts ──────────────────────────────────────────────────────────────────
with tab_concepts:
    st.subheader("Concepts")

    search = st.text_input("Search concepts", placeholder="e.g. ideal gas, entropy …")

    concepts = ontology.get_concepts(filter=search)
    # concepts = [
    #     {"name": "Ideal Gas", "description": "A gas that follows the ideal gas law PV = nRT.", "related": ["Pressure", "Volume", "Temperature"]},
    #     {"name": "Entropy", "description": "A measure of disorder or randomness in a thermodynamic system.", "related": ["Heat", "Temperature"]},
    #     {"name": "Enthalpy", "description": "Total heat content of a system at constant pressure.", "related": ["Internal Energy", "Pressure", "Volume"]},
    # ]

    if search:
        concepts = [c for c in concepts if search.lower() in c["name"].lower() or search.lower() in c["description"].lower()]

    if not concepts:
        st.warning("No concepts match the search term.")
    else:
        for concept in concepts:
            with st.expander(concept["name"]):
                st.write(concept["description"])
                if concept.get("related"):
                    family_relations = ontology.get_family_of_concept(concept["name"])
                    if family_relations["parent"]:
                        st.markdown("**Parent Class:** " + list_to_nice_string(family_relations["parent"]))
                    if family_relations["children"]:
                        st.markdown("**Children Classes:** " + list_to_nice_string(family_relations["children"]))
                    st.markdown("**Related concepts:** " + list_to_nice_string(concept["related"]["concepts"]))
                    st.markdown("**Related variables:** " + list_to_nice_string(concept["related"]["variables"]))
                    st.markdown("**Related equations:** " + list_to_nice_string(concept["related"]["equations"]))

# ── Variables ─────────────────────────────────────────────────────────────────
with tab_variables:
    st.subheader("Variables")

    search_var = st.text_input("Search variables", placeholder="e.g. pressure, temperature …")

    variables = ontology.get_variables(filter=search_var)
    # variables = [
    #     {"symbol": "P", "name": "Pressure", "unit": "Pa", "description": "Force per unit area exerted by a gas."},
    #     {"symbol": "V", "name": "Volume", "unit": "m³", "description": "Amount of space occupied by the gas."},
    #     {"symbol": "T", "name": "Temperature", "unit": "K", "description": "Average kinetic energy of the particles."},
    #     {"symbol": "n", "name": "Amount of substance", "unit": "mol", "description": "Number of moles of gas."},
    #     {"symbol": "U", "name": "Internal Energy", "unit": "J", "description": "Total energy stored within a system."},
    #     {"symbol": "H", "name": "Enthalpy", "unit": "J", "description": "H = U + PV"},
    #     {"symbol": "S", "name": "Entropy", "unit": "J/K", "description": "Measure of disorder in a system."},
    # ]

    if search_var:
        variables = [
            v for v in variables
            if search_var.lower() in v["name"].lower()
            or search_var.lower() in v["symbol"].lower()
        ]

    if not variables:
        st.warning("No variables match the search term.")
    else:
        import pandas as pd
        df = pd.DataFrame(variables)[["symbol", "name", "unit", "value"]]
        df.columns = ["Symbol", "Name", "SI Unit", "Default value"]
        st.dataframe(df, width='stretch', hide_index=True)

# ── Equations ─────────────────────────────────────────────────────────────────
with tab_equations:
    st.subheader("Equations")

    search_eq = st.text_input("Search equations", placeholder="e.g. ideal gas law, first law …")

    equations = ontology.get_equations(filter=search_eq)

    if search_eq:
        equations = [
            e for e in equations
            if search_eq.lower().replace(' ', '') in e["name"].lower()
            or search_eq.lower() in e["expression"].lower()
        ]

    if not equations:
        st.warning("No equations match the search term.")
    else:
        for eq in equations:
            if eq["name"] != "AdditionalEquation":
                with st.expander(f"**{camel_to_normal(eq['name'])}** — `{eq['expression']}`"):
                    st.markdown(f"**Name:** {camel_to_normal(eq["name"])}")
                    st.markdown(f"**Expression:** `{eq['expression']}`")
                    # st.markdown("**Variables involved:** " + list_to_nice_string(eq["name"]))
                    if eq["slots"]:
                        st.markdown(f"**Required Concepts:** {list_to_nice_string(eq["slots"], camel=True)}")
                    else:   
                        st.markdown(f"**Required Concepts:** None")
                    if eq["rules"]:
                        st.markdown("Equation applies when the following conditions are met: " + list_to_nice_string(eq["rules"]))
                    else:
                        st.markdown("Equation applies without any constraints.")

# ── Graph view ────────────────────────────────────────────────────────────────
with tab_graph:
    st.subheader("Ontology graph")
    # st.info(
    #     "You can view the ontology as a graph here.",
    #     # icon="💡",
    # )

    toggle_columns = st.columns(4)
    show_concepts = toggle_columns[0].toggle("Concepts", value=True)
    show_variables = toggle_columns[1].toggle("Variables", value=True)
    show_equations = toggle_columns[2].toggle("Equations", value=True)
    show_rules = toggle_columns[3].toggle("Rules", value=True)

    nodes = []
    node_ids = set()
    edges = []
    colors = {
        "concepts": "#C35CFA",
        "variables": "#FA745C",
        "equations": "#5CE2FA",
        "rules": "#93FA5C",
    }

    def add_node(node_id, label, category):
        if node_id not in node_ids:
            nodes.append(Node(id=node_id, label=label, color=colors[category]))
            node_ids.add(node_id)

    if show_concepts:
        for c in concepts:
            add_node(c["name"], c["name"], "concepts")
            if "related" in c:
                if show_concepts:
                    edges += [
                        Edge(source=c["name"], target=related, label="has")
                        for related in c["related"]["concepts"]
                    ]
                if show_variables:
                    edges += [
                        Edge(source=c["name"], target=related.split(" ")[0], label="is defined by")
                        for related in c["related"]["variables"]
                    ]
                if show_equations:
                    edges += [
                        Edge(source=snake_to_camel(related), target=c["name"], label="applies to")
                        for related in c["related"]["equations"]
                    ]

    if show_equations:
        for eq in equations:
            add_node(eq["name"], eq["name"], "equations")
            if show_rules and eq["rules"]:
                for rule in eq["rules"]:
                    add_node(rule, rule, "rules")
                    edges.append(Edge(source=eq["name"], target=rule, label="is constrained by"))

    if show_variables:
        for v in variables:
            add_node(v["name"], f"{v['name']} *{v['symbol']}*", "variables")

    config = Config(width="100%", height=600, directed=True)
    agraph(nodes=nodes, edges=edges, config=config)