"""
KnowTD – Thermodynamics Knowledge Tool
Main entry point for the Streamlit app.
"""

import streamlit as st

st.set_page_config(
    page_title="KnowTD",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Sidebar branding ──────────────────────────────────────────────────────────
st.sidebar.title("🌡️ KnowTD")
st.sidebar.caption("Thermodynamics Knowledge Tool")
st.sidebar.divider()

# ── Home page content ─────────────────────────────────────────────────────────
st.title("Welcome to KnowTD")
st.subheader("A knowledge-driven tool for thermodynamics")

st.markdown(
    """
    This interface lets you explore and interact with a thermodynamics ontology
    and the reasoning engine built on top of it.

    **Choose a section from the sidebar to get started:**
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        "### 🗂️ Ontology\n"
        "Browse concepts, variables, and equations stored in the thermodynamics ontology.",
        icon=None,
    )

with col2:
    st.info(
        "### ✏️ Solve Exercise\n"
        "Enter a thermodynamics exercise – via a structured form or in plain natural language – "
        "and let the reasoning engine compute the missing values.",
        icon=None,
    )

with col3:
    st.info(
        "### 🔭 Exercise Space\n"
        "Explore the full space of possible exercises that can be derived from the ontology "
        "and generate new exercises automatically.",
        icon=None,
    )

st.divider()
st.caption("Navigate using the **sidebar** on the left.")
