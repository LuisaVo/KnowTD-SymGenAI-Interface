"""
KnowTD – Thermodynamics Knowledge Tool
Main entry point for the Streamlit app.
"""

import base64
from pathlib import Path

import streamlit as st

HERO_IMAGE_PATH = Path("assets/WebsiteHeader.png")
LOGO_PATH = Path("assets/Logo.svg")

st.set_page_config(
    page_title="KnowTD",
    page_icon=str(LOGO_PATH) if LOGO_PATH.exists() else None,
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Sidebar branding ──────────────────────────────────────────────────────────


def encode_image_base64(image_path: Path) -> str:
    if not image_path.exists():
        return ""
    return base64.b64encode(image_path.read_bytes()).decode("utf-8")


hero_image_base64 = encode_image_base64(HERO_IMAGE_PATH)
logo_image_base64 = encode_image_base64(LOGO_PATH)

# ── Sidebar branding ──────────────────────────────────────────────────────────
sidebar_brand = (
    f'<img src="data:image/svg+xml;base64,{logo_image_base64}" '
    'style="width: 28px; height: 28px;" alt="KnowTD logo">'
    if logo_image_base64
    else ""
)
st.sidebar.markdown(
    f"""
    <div style="display:flex; align-items:center; gap:0.65rem; margin-bottom:0.35rem;">
        {sidebar_brand}
        <div style="font-size:1.4rem; font-weight:700; color:#1f1f1f;">KnowTD</div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.sidebar.caption("KnowTD translates natural-language thermodynamics problems into structured representations, validates them against an ontology, and solves them using symbolic reasoning.")
st.sidebar.divider()

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,500,0,0');

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
    .hero-section {
        text-align: center;
        padding: 3rem 1.5rem;
        border-radius: 24px;
        margin-bottom: 2rem;
        background-size: cover;
        background-position: center;
        overflow: hidden;
        position: relative;
        min-height: 380px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .hero-overlay {
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, rgba(255,255,255,0.90), rgba(255,255,255,0.72));
    }
    .hero-content {
        position: relative;
        z-index: 1;
        max-width: 900px;
        width: 100%;
    }
    .header-title {
        font-size: 2.6rem;
        font-weight: 700;
        margin: 0.5rem 0;
        color: #1f1f1f;
    }
    .hero-title-row {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 0.75rem;
        flex-wrap: wrap;
    }
    .hero-title-logo {
        width: 55px;
        height: 55px;
    }
    .header-subtitle {
        font-size: 1.05rem;
        color: #4f5a67;
        margin: 0.5rem auto 1rem auto;
        max-width: 760px;
    }
    .hero-description {
        font-size: 0.98rem;
        color: #4f5a67;
        line-height: 1.65;
        max-width: 800px;
        margin: 0 auto 1.5rem auto;
    }
    .hero-buttons {
        position: relative;
        z-index: 1;
    }
    .process-flow {
        display: flex;
        align-items: center;
        justify-content: space-around;
        margin: 2rem 0;
        flex-wrap: wrap;
        gap: 0.5rem;
    }
    .flow-step {
        display: flex;
        flex-direction: column;
        justify-content: top;
        align-items: center;
        text-align: center;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 8px;
        min-width: 140px;
        height: 185px;
        font-size: 0.9rem;
    }
    .flow-arrow {
        font-size: 1.5rem;
        color: #999;
    }
    .flow-icon {
        font-family: 'Material Symbols Outlined';
        font-size: 2.5rem;
        line-height: 1;
        color: #343deb;
        margin-bottom: 0.45rem;
    }
    .cards-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))
        gap: 1.5rem;
        margin: 2rem 0;
    }
    .card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #0066cc;
    }
    .card-title {
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #1f1f1f;
    }
    .card-description {
        font-size: 0.95rem;
        color: #555;
        margin-bottom: 1rem;
    }
    .features {
        display: flex;
        gap: 1.5rem;
        margin: 1.5rem 0;
        flex-wrap: wrap;
    }
    .feature {
        flex: 1;
        min-width: 200px;
        padding: 1rem;
        border-radius: 8px;
        background: #fff;
        border: 1px solid #e0e0e0;
    }
    .feature-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    .feature-title {
        font-weight: 600;
        margin: 0.5rem 0;
    }
    .why-container {
        display: flex;
        gap: 2rem;
        margin: 2rem 0;
        align-items: start;
    }
    .why-content {
        flex: 1;
    }
    .why-points {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }
    .why-point {
        display: flex;
        gap: 1rem;
        align-items: start;
    }
    .why-point-title {
        font-weight: 600;
        min-width: 100px;
    }
    .example-section {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 2rem 0;
    }
    .feature-main-card {
        background: #f8f9fa;
        border: 1px solid #e7ebf2;
        border-radius: 12px;
        padding: 1rem 1rem 0.9rem 1rem;
        # height: 400px;
        # overflow-y: auto;
    }
    .feature-main-title {
        font-size: 1.28rem;
        font-weight: 700;
        margin-bottom: 0.65rem;
    }
    .feature-main-text {
        color: #4f5a67;
        line-height: 1.58;
        font-size: 0.94rem;
    }
    .feature-main-title-solve { color: #343deb; }
    .feature-main-title-ontology { color: #2DA2AB; }
    .feature-main-title-generate { color: #746CFF; }
    .st-key-main_feature_solve div.stButton > button {
        background: #e9ebff !important;
        color: #343deb !important;
        border: 1px solid #d2d7ff !important;
    }
    .st-key-main_feature_solve div.stButton > button:hover {
        background: #dfe3ff !important;
        color: #343deb !important;
        border-color: #c6ceff !important;
    }
    .st-key-main_feature_ontology div.stButton > button {
        background: #dbf4f6 !important;
        color: #2DA2AB !important;
        border: 1px solid #c2ecef !important;
    }
    .st-key-main_feature_ontology div.stButton > button:hover {
        background: #d0eef1 !important;
        color: #2DA2AB !important;
        border-color: #b5e4e8 !important;
    }
    .st-key-main_feature_generate div.stButton > button {
        background: #ece9ff !important;
        color: #746CFF !important;
        border: 1px solid #dad4ff !important;
    }
    .st-key-main_feature_generate div.stButton > button:hover {
        background: #e3defd !important;
        color: #746CFF !important;
        border-color: #cdc3ff !important;
    }
    </style>
""", unsafe_allow_html=True)

# ── Header Section ────────────────────────────────────────────────────────────
hero_style = (
    f'background-image: url("data:image/png;base64,{hero_image_base64}");'
    if hero_image_base64
    else "background: linear-gradient(135deg, #eef3ff, #f9fbff);"
)

hero_title_logo = (
    f'<img src="data:image/svg+xml;base64,{logo_image_base64}" class="hero-title-logo" alt="KnowTD logo">'
    if logo_image_base64
    else ""
)

st.markdown(
    f"""
    <div class="hero-section" style='{hero_style}'>
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <div class="hero-title-row">
                {hero_title_logo}
                <div class="header-title">KnowTD Interface</div>
            </div>
            <div class="header-subtitle">Natural-language access to ontology-grounded thermodynamics reasoning</div>
            <p class="hero-description">
                Enter a thermodynamics problem in plain language. The LLM proposes a structured interpretation
                in YAML, which is validated against the KnowTD ontology. Valid problems are solved using
                symbolic thermodynamic reasoning to produce results, equations, and a reasoning graph.
            </p>
        </div>
    </div>
    <div class="hero-buttons">
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Try an Example Exercise", key="btn_example", use_container_width=True):
        st.switch_page("pages/0_Try_an_Example.py")
with col2:
    if st.button("Solve Your Own Problem", key="btn_solve", use_container_width=True):
        st.switch_page("pages/1_Solve_Text_Input.py")
with col3:
    if st.button("Explore the Ontology", key="btn_ontology", use_container_width=True):
        st.switch_page("pages/5_Explore_Ontology.py")

st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ── How It Works Flow ─────────────────────────────────────────────────────────
st.markdown("## How it works")
st.caption("Follow this workflow from left to right to understand how a thermodynamics problem is parsed and solved.")
st.markdown("""
    <div class="process-flow">
        <div class="flow-step">
            <div class="flow-icon">chat</div>
            <strong>Problem Text</strong>
            <div style="font-size: 0.8rem; color: #666;">Natural-language<br>thermodynamics<br>problem</div>
        </div>
        <div class="flow-arrow">→</div>
        <div class="flow-step">
            <div class="flow-icon">network_intel_node</div>
            <strong>LLM Parser</strong>
            <div style="font-size: 0.8rem; color: #666;">Proposes a structured<br>interpretation</div>
        </div>
        <div class="flow-arrow">→</div>
        <div class="flow-step">
            <div class="flow-icon">edit_document</div>
            <strong>Editable YAML</strong>
            <div style="font-size: 0.8rem; color: #666;">Review and edit<br>the generated<br>YAML</div>
        </div>
        <div class="flow-arrow">→</div>
        <div class="flow-step">
            <div class="flow-icon">verified</div>
            <strong>Validation</strong>
            <div style="font-size: 0.8rem; color: #666;">Validate against<br>the KnowTD<br>ontology</div>
        </div>
        <div class="flow-arrow">→</div>
        <div class="flow-step">
            <div class="flow-icon">emoji_objects</div>
            <strong>KnowTD Reasoner</strong>
            <div style="font-size: 0.8rem; color: #666;">Symbolic thermodynamic<br>reasoning</div>
        </div>
        <div class="flow-arrow">→</div>
        <div class="flow-step">
            <div class="flow-icon">query_stats</div>
            <strong>Solution</strong>
            <div style="font-size: 0.8rem; color: #666;">Results, equations<br>and reasoning<br>graph</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.divider()

# ── Three Main Features ───────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-main-card">
            <div class="feature-main-title feature-main-title-solve">Solve Exercise</div>
            <div class="feature-main-text">
                Parse textbook problems into structured YAML, validate them against the ontology,
                and compute the solution with symbolic thermodynamic reasoning.
                <br><br>
    There are 3 access points:
    
    - **Text Input** is best for: Fast answers, classroom demos, textbook problems
    - **Form Input** is best for: Understanding, debugging, experimentation
    - **File Input** is best for: Batch solving, validation, pipelines

    No matter the input, the system provides the numerical solution as well as the solution path and the full reasoning graph. 
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    if st.button("Open Solve Exercise", key="main_feature_solve", use_container_width=True):
        st.switch_page("pages/1_Solve_Text_Input.py")

with col2:
    st.markdown(
        """
        <div class="feature-main-card">
            <div class="feature-main-title feature-main-title-ontology">Explore Ontology</div>
            <div class="feature-main-text">
                Inspect the domain model behind the solver.
                Browse concepts, variables, equations, and constraints to understand
                when each relationship applies.
    
    - **Browse concepts** with descriptions (e.g., "adiabatic process", "isentropic expansion")
    - **Explore variables** with their symbols, units, and typical ranges
    - **Review equations** that define relationships between variables
    - **Inspect constraints** and rules that govern when equations apply
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.space("xsmall")
    if st.button("Open Explore Ontology", key="main_feature_ontology", use_container_width=True):
        st.switch_page("pages/5_Explore_Ontology.py")

with col3:
    st.markdown(
        """
        <div class="feature-main-card">
            <div class="feature-main-title feature-main-title-generate">Generate Exercises</div>
            <div class="feature-main-text">
                Explore scenario templates and generate complete exercises with solutions.
                Review resulting values, equations, and graph-based reasoning in one place.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.space("xsmall")
    if st.button("Open Generate Exercises", key="main_feature_generate", use_container_width=True):
        st.switch_page("pages/4_Generate_Exercises.py")

st.divider()

# ── About This Project ────────────────────────────────────────────────────────
st.markdown("## About this project")

col_about_text, col_about_features = st.columns([1, 1])

with col_about_text:
    st.markdown("""
    This interface helps you work with thermodynamics problems in a more 
    accessible way. You can enter a problem in natural language, inspect the 
    structured YAML representation, and solve it with KnowTD.

    The language model helps translate text into structure, while validation 
    and thermodynamic reasoning are handled by the ontology-based KnowTD system.
    You stay in control by reviewing and editing the generated representation 
    before solving.
    """)

with col_about_features:
    st.markdown("""
    **Natural-language input**  
    Start from textbook-style thermodynamics problems instead of writing YAML by hand.

    **Human-in-the-loop**  
    Inspect and edit the generated YAML before it is validated and solved.

    **Transparent reasoning**  
    View computed values, selected equations, solution paths, and reasoning graphs.
    """)

st.divider()

# ── Example Preview ───────────────────────────────────────────────────────────
st.markdown("## Example preview")

example_col1, example_col2, example_col3 = st.columns(3)

with example_col1:   
    example_text = """A gas in rigid tank with the volume $V = 0.05\,\mathrm{m^3}$ is stirred. 
The initial temperature and pressure are $T_1 = 315\,\mathrm{K}$ and $p_1 = 1\,\mathrm{bar}$. 
The stirrer supplies a work of $0.5\,\mathrm{kJ}$. 
The tank is cooled, as there is a threshold for the final temperature.

Calculate the heat that is removed if the final temperature is $T_2 = 320\,\mathrm{K}$. 

The gas is ideal, with $R = 287\,\mathrm{J/(kg\,K)}$ and $c_v = 1010\,\mathrm{J/(kg\,K)}$."""    
    
    st.markdown(f"""
    **Problem (text)**
    
{example_text}
    """)
    
    if st.button(f"Run the example", use_container_width=True):
                    # Store in session state for the Solve Text Input page to pick up
                    st.session_state["exercise_text"] = example_text
                    st.session_state["selected_example_label"] = "Problem6"
                    st.switch_page("pages/1_Solve_Text_Input.py")

with example_col2:
    st.markdown("""
    **Parsed YAML (excerpt)**
    
    ```yaml
    problem_class: SingleStep
    states:
    - id: 1
        V:
        value: 0.05
        T:
        value: 315
        p:
        value: 100000
    - id: 2
        T:
        value: 320
    transition:
    is_isochoric: true
    W:
      value: 500
    required_variables:
    - Q_12
    ```
    """)

with example_col3:
    st.markdown("""
    **Result (value and solution path)**

    $Q = −220.70\,\mathrm{J}$
    """)
    st.image("assets/SP-Problem6.png", width="stretch")

st.divider()
st.markdown("""
<div style="text-align: center; color: #999; padding: 1.5rem; font-size: 0.9rem;">
Built with Streamlit
</div>
""", unsafe_allow_html=True)

# ── Publications ──────────────────────────────────────────────────────────────
st.markdown("## Research behind this interface")

st.markdown("""
This interface builds on a series of publications about making thermodynamic
knowledge computable, explainable, and useful for education.
""")

pub_col1, pub_col2, pub_col3 = st.columns(3)

with pub_col1:
    st.markdown("### KnowTD")
    st.markdown("""
    The original KnowTD paper describes how thermodynamic knowledge can be
    translated into an actionable knowledge-based system.
    """)
    st.link_button(
        "Read the KnowTD paper",
        "https://pubs.acs.org/doi/10.1021/acs.jcim.4c00647"
    )

with pub_col2:
    st.markdown("### Knowledge-Graph Reasoning")
    st.markdown("""
    This work explains how KnowTD uses ontologies and knowledge graphs to set up
    thermodynamics problems and produce transparent solution paths.
    """)
    st.link_button(
        "Read the KG reasoning paper",
        "https://ceur-ws.org/Vol-3977/XAIKG-3.pdf"
    )

with pub_col3:
    st.markdown("### Exercise Generation")
    st.markdown("""
    This work combines formal reasoning and KnowTD to generate plausible
    thermodynamics exercise scenarios, assign values, and compute sample solutions.
    """)
    st.link_button(
        "Read the exercise generation preprint",
        "https://www.researchsquare.com/article/rs-8989074/v1"
    )

st.divider()


# Built with Streamlit • Header designed by <a href="https://www.magnific.com"> Magnific</a>
