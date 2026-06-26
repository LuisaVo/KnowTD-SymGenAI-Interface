from pathlib import Path

import streamlit as st


def load_styles() -> None:
    st.markdown("""
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
    div.stDownloadButton > button:hover {
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
    div.stButton > button[kind="primary"] {
        background: #343deb !important;
        color: #ffffff !important;
        border: 1px solid #343deb !important;
        border-radius: 10px;
        font-weight: 600;
    }
    div.stButton > button[kind="primary"]:hover {
        background: #2b33c7 !important;
        border-color: #2b33c7 !important;
        color: #ffffff !important;
    }
    div.stButton > button[kind="secondary"] {
        background: #FFFFFF !important;
        color: #343deb !important;
        border: 1px solid #a9aceb !important;
        border-radius: 10px;
        font-weight: 600;
    }
    div.stButton > button[kind="secondary"]:hover {
        background: #9da2e3 !important;
        border-color: #9da2e3 !important;
        color: #343deb !important;
    }
    .steps-flow-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 0.6rem;
        margin: 0.5rem 0 0.75rem 0;
    }
    .steps-flow-step {
        background: #f8f9fa;
        padding: 0.9rem;
        background: #f8f9fa;
        border-radius: 8px;
    }
    .steps-flow-step strong {
        display: block;
        margin-bottom: 0.2rem;
    }
    .steps-flow-step span {
        color: #616161;
        font-size: 0.84rem;
    }
    .example-card {
        border: 1px solid #eceff4;
        border-radius: 10px;
        background: #f8f9fa;
        padding: 0.75rem;
        margin-bottom: 0.6rem;
    }
    .example-textbox {
        height: 120px;
        overflow-y: auto;
        white-space: pre-wrap;
        line-height: 1.35;
        font-size: 0.92rem;
        color: #2f2f2f;
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
    .nl-flow-step span {
        font-size: 0.8rem;
        color: #666;
        line-height: 1.3;
    }
    .nl-flow-arrow {
        font-size: 1.3rem;
        color: #999;
    }
    </style>
    """,
    unsafe_allow_html=True,
)