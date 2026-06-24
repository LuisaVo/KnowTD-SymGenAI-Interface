"""
Try an Example
Explore sample thermodynamics problems and see them solved step-by-step.
"""

import streamlit as st
import yaml
from pathlib import Path

st.set_page_config(
    page_title="Try an Example | KnowTD",
    page_icon="assets/Logo.svg",
    layout="wide",
)

st.title("▶ Try an Example Exercise")
st.markdown("Click on any example problem below to see it solved step-by-step with full reasoning.")
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
    .example-flow-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 0.6rem;
        margin: 0.5rem 0 0.75rem 0;
    }
    .example-flow-step {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 0.85rem;
        border: 1px solid #eceff4;
    }
    .example-flow-step strong {
        display: block;
        margin-bottom: 0.2rem;
    }
    .example-flow-step span {
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
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown("### Workflow")
st.caption("Pick a sample, open it in the text solver, then parse and inspect the full solution pipeline.")
st.markdown(
    """
    <div class="example-flow-grid">
        <div class="example-flow-step"><strong>1. Select</strong><span>Choose a sample problem card.</span></div>
        <div class="example-flow-step"><strong>2. Open</strong><span>Load it directly into the text input solver.</span></div>
        <div class="example-flow-step"><strong>3. Solve</strong><span>Convert to YAML and compute the answer.</span></div>
        <div class="example-flow-step"><strong>4. Inspect</strong><span>Review values, equations, and reasoning graph.</span></div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# Load example problems from the markdown file
EXAMPLE_FILE = Path("utils/DescriptionSampleProblems.md")

def load_examples_from_markdown(markdown_path: Path) -> dict[str, str]:
    """Parse markdown sections in the form '## ProblemX' into label->text map."""
    if not markdown_path.exists():
        return {}
    
    import re
    content = markdown_path.read_text(encoding="utf-8")
    parts = re.split(r"^##\s+(Problem\d+)\s*$", content, flags=re.MULTILINE)
    examples: dict[str, str] = {}
    for i in range(1, len(parts), 2):
        name = parts[i].strip()
        body = parts[i + 1].strip()
        if body:
            examples[name] = body
    return examples

examples = load_examples_from_markdown(EXAMPLE_FILE)
example_labels = sorted(examples.keys(), key=lambda x: int(x.replace("Problem", "")))

if not examples:
    st.warning("Could not load example problems. Check that utils/DescriptionSampleProblems.md exists.")
else:
    st.markdown("## Available Examples")
    
    # Create a grid of example cards
    cols_per_row = 3
    for i in range(0, len(example_labels), cols_per_row):
        cols = st.columns(cols_per_row)
        for col_idx, label in enumerate(example_labels[i:i+cols_per_row]):
            with cols[col_idx]:
                problem_text = examples[label]
                st.markdown(
                    f"""
                    <div class="example-card">
                        <strong>{label}</strong>
                        <div class="example-textbox">{problem_text}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                
                if st.button(f"Try {label}", key=f"btn_{label}", use_container_width=True):
                    # Store in session state for the Solve Text Input page to pick up
                    st.session_state["exercise_text"] = problem_text
                    st.session_state["selected_example_label"] = label
                    st.switch_page("pages/1_Solve_Text_Input.py")
                st.space("small")

st.divider()

st.markdown("""
## How It Works

1. **Click** on an example problem above
2. You'll be taken to the **Solve – Text Input** page with the problem pre-loaded
3. **Choose** an LLM model and provide your API key
4. **Click "Parse & Solve"** to parse and solve the problem
5. **Review** the computed values, solution path, and reasoning graph

## Need Help?

- Check the **Explore Ontology** page to understand thermodynamics concepts
- Visit **Generate Exercises** to create your own problems automatically
- See the **Solve Exercise** options for different input methods
""")
