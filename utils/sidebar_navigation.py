from __future__ import annotations

import base64
from pathlib import Path

import streamlit as st


_BRAND_CAPTION = (
    "KnowTD translates natural-language thermodynamics problems into structured "
    "representations, validates them against an ontology, and solves them using "
    "symbolic reasoning."
)


def _encode_image_base64(image_path: Path) -> str:
    if not image_path.exists():
        return ""
    return base64.b64encode(image_path.read_bytes()).decode("utf-8")


def _find_logo_path() -> Path | None:
    for candidate in (Path("assets/Logo2.svg"), Path("assets/Logo.svg")):
        if candidate.exists():
            return candidate
    return None


def render_sidebar_navigation() -> None:
    logo_path = _find_logo_path()
    logo_base64 = _encode_image_base64(logo_path) if logo_path else ""
    sidebar_brand = (
        f'<img src="data:image/svg+xml;base64,{logo_base64}" '
        'style="width: 28px; height: 28px;" alt="KnowTD logo">'
        if logo_base64
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
    st.sidebar.caption(_BRAND_CAPTION)
    st.sidebar.divider()

    st.sidebar.page_link(
        "Overview.py",
        label="Overview",
        icon=":material/home:",
        use_container_width=True,
    )

    st.sidebar.markdown("**Solve**")
    st.sidebar.page_link(
        "pages/1_Solve_Text_Input.py",
        label="Text Input",
        icon=":material/chat:",
        use_container_width=True,
    )
    st.sidebar.page_link(
        "pages/2_Solve_Form_Input.py",
        label="Form Input",
        icon=":material/dashboard_customize:",
        use_container_width=True,
    )
    st.sidebar.page_link(
        "pages/3_Solve_File_Input.py",
        label="File Input",
        icon=":material/upload_file:",
        use_container_width=True,
    )

    st.sidebar.markdown("**Explore**")
    st.sidebar.page_link(
        "pages/0_Try_an_Example.py",
        label="Try an Example",
        icon=":material/rocket_launch:",
        use_container_width=True,
    )
    st.sidebar.page_link(
        "pages/4_Generate_Exercises.py",
        label="Generate Exercises",
        icon=":material/auto_awesome:",
        use_container_width=True,
    )
    st.sidebar.page_link(
        "pages/5_Explore_Ontology.py",
        label="Explore Ontology",
        icon=":material/schema:",
        use_container_width=True,
    )
