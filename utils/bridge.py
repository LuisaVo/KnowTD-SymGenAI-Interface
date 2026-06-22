"""
utils/bridge.py
===============
Adapter layer between the Streamlit interface and the Python backend.

All functions should return plain Python dicts / lists / DataFrames so the
UI pages stay decoupled from the backend implementation.
"""

from __future__ import annotations
from typing import Any
from linkml_runtime.utils.schemaview import SchemaView, SlotDefinition
from mistralai.client import Mistral
from openai import OpenAI 
import graphviz
import json
from streamlit_agraph import Node, Edge

import sys
sys.path.append('exercise-generation/scripts')
import GenerateProblem

try:
    from OutputRendering import latex_typsetting
except Exception:
    def latex_typsetting(formula):
        return formula

# ---------------------------------------------------------------------------
# Imports – uncomment and adjust once you connect your real backend
# ---------------------------------------------------------------------------
# import sys, os
# sys.path.insert(0, os.path.abspath("path/to/your/backend"))
#
# from your_ontology_module import ThermodynamicsOntology
# from your_solver_module    import Solver
# from your_generator_module import ExerciseGenerator
# from your_nl_parser_module import NLParser

# ===========================================================================
# 1. Ontology
# ===========================================================================

class Ontology:
    def __init__(self, filename="knowtd/Ontology/thermodynamics_ontology.yaml"):
        self.schemaview = SchemaView(filename)

    def get_concepts(self, filter: str = "") -> list[dict]:
        """Return a list of concepts with their name, description, and related variables."""
        concepts = []
        for concept in self.schemaview.class_descendants("Concept", reflexive=False):
            class_def = self.schemaview.get_class(concept)
            if not class_def.abstract:                
                concepts.append({
                    "name": concept,
                    "description": class_def.description,
                    "related": self.sort_slots_by_type(class_def.slots),
                })
        return concepts
    
    def get_variables(self, filter: str = "") -> list[dict]:
        """Return a list of variables with their symbol, name, unit, and description."""
        variables = []
        for variable in self.schemaview.class_descendants("Variable", reflexive=False):
            class_def = self.schemaview.get_class(variable)
            if not class_def.abstract:
                variables.append({
                    "symbol": class_def.annotations['schema:mathExpression']['value'] if class_def.annotations and 'schema:mathExpression' in class_def.annotations else '',
                    "name": variable,
                    "unit": class_def.annotations['schema:Unit']['value'] if class_def.annotations and 'schema:Unit' in class_def.annotations else '',
                    "description": class_def.description,
                    "value": eval(class_def.slot_usage.get('value').ifabsent) if class_def.slot_usage else None,
                })
        return variables
    
    def get_equations(self, filter: str = "") -> list[dict]:
        """Return a list of equations with their name, expression, and rules."""
        equations = []
        all_rules = set(self.schemaview.class_descendants("Rule", mixins=False, reflexive=False))
        for equation in self.schemaview.class_descendants("Equation", reflexive=False):
            class_def = self.schemaview.get_class(equation)
            if not class_def.abstract:
                rules = [a for a in self.schemaview.class_ancestors(equation, mixins=True, is_a=True, reflexive=False) if a in all_rules]
                equations.append({
                    "name": equation,
                    "expression": class_def.annotations['schema:mathExpression']['value'] if class_def.annotations and 'schema:mathExpression' in class_def.annotations else '',
                    "rules": rules,
                    "slots": [s.range for s in self.schemaview.class_induced_slots(equation) if "equation_references" in s.in_subset]
                })
        return equations
    
    def get_problem_classes(self) -> list[dict]:
        """Return a list of all problem classes defined in the ontology."""
        problems = []
        for problem in self.schemaview.class_descendants("Problem", reflexive=False):
            class_def = self.schemaview.get_class(problem)
            if not class_def.abstract:
                problems.append({
                    "name": problem,
                    "description": class_def.description,
                })
        return problems
    
    def sort_slots_by_type(self, slots: list):
        """Given slots of a class, returns them sorted by concept, variable or equation (range)"""
        result = {"concepts": [],
                  "variables": [],
                  "equations": []}
        for slot_name in slots:
            if not slot_name == 'id':
                slot_range = self.schemaview.get_slot(slot_name).range
                if slot_range and \
                    (not slot_range in ['boolean', 'string', 'float', 'integer']) and \
                    (not slot_range in self.schemaview.all_enums()):
                        ancestors = self.schemaview.class_ancestors(slot_range)
                        if 'Concept' in ancestors:
                            result["concepts"].append(slot_name)
                        elif 'Variable' in ancestors:
                            result["variables"].append(f"{slot_range} *{slot_name}*")
                        elif 'Equation' in ancestors:
                            result["equations"].append(slot_name)
        return result


# ===========================================================================
# 2. Solver
# ===========================================================================




# ===========================================================================
# 3. Natural language parser
# ===========================================================================
def get_prompt(user_text: str) -> str:
    yaml_template = open("utils/Template_SingleStep.yaml").read()
    return f"""
    *Task:* 
    Fill in the provided JSON template using only the information from the problem statement.
    
    *Rules:*
    - Only use given values from the problem statement.
    - Keep unknown values as None.
    - Use the specific or total form of properties as appropriate (e.g., v for specific volume, V for total volume, w for mass specific work and q for mass specific heat).
    - Keep the structure of the JSON exactly as provided.
    - Analyze the problem statement to identify if the problem is adiabatic, reversible, isobaric, isochoric, and so on.
    - The "required_variables" field must list the IDs of the variables explicitly asked for in the problem.
    - Do not calculate or infer additional values.
    
    *Problem Statement:* 
    {user_text}
    
    *JSON Template:*
    {yaml_template}
    """

def chat_call(prompt: str, api_key: str, model: str = "mistral-large-latest") -> str:
    "call the corresponding model to translate the problem into the YAML format"
    res = ''
    if "mistral" in model:
        res = chat_mistral(prompt, api_key, model)
    elif "gpt" in model:
        res = chat_openai(prompt, api_key, model)
    return response_to_yaml_dict(res)

def chat_mistral(prompt: str, api_key: str, model: str = "mistral-large-latest") -> str:
    """
    Use a Mistral model to translate the problem into the YAML format.
    """
    client = Mistral(api_key=api_key)
    chat_response = client.chat.complete(
        model = model,
        messages = [
            {
                "role": "user",
                "content": get_prompt(prompt)
            }
        ],
        response_format={ "type": "json_object" }
    )
    
    return chat_response.choices[0].message.content

def chat_openai(prompt: str, api_key: str, model: str) -> str:
    """
    Use a openai model to translate the problem into the YAML format.
    """
    client = OpenAI(api_key=api_key)
    response = client.responses.create(
                model=model,
                input=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant designed to output JSON."
                    },
                    {
                        "role": "user",
                        "content": get_prompt(prompt)
                    }
                ],
                text={"format": {"type": "json_object"}}
                )
    
    return response.output_text


def validate_credentials(api_key: str, model: str = "mistral-large-latest") -> tuple[bool, str]:
    """
    Validate that the provided API key can access the selected model.
    """
    try:
        if not api_key or not api_key.strip():
            return False, "API key is empty."

        if 'mistral' in model:
            client = Mistral(api_key=api_key.strip())
            client.chat.complete(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": "ping",
                    }
                ],
                max_tokens=1,
            )
            return True, "Credentials are valid."
        else:
            client = OpenAI(api_key=api_key.strip())
            client.responses.create(
                model=model,
                input=[
                    {
                        "role": "user",
                        "content": "ping",
                    }
                ],
            )
            return True, "Credentials are valid."
        
    except Exception as exc:
        return False, str(exc)

def graph_to_chat(graph: dict, api_key: str) -> str:
    pass
    
    
def response_to_yaml_dict(response: str) -> dict:
    """
    Convert the response string into a Python dictionary.
    """
    dict_response = json.loads(response.replace('"True"', 'true').replace('"False"', 'false'))
    def remove_none_values(data):
        """Recursively remove keys with None values from nested JSON."""
        if isinstance(data, dict):
            return {k: remove_none_values(v) for k, v in data.items() if not isinstance(v, str) or isinstance(v, str) and "None" not in v and "null" not in v}
        elif isinstance(data, list):
            return [remove_none_values(item) for item in data if item is not None]
        else:
            return data
    return remove_none_values(dict_response)

# ===========================================================================
# 4. Exercise space
# ===========================================================================

def get_exercise_space_stats() -> dict:
    """Return summary statistics about the full exercise space."""
    # TODO: return your generator's stats
    raise NotImplementedError


def filter_exercises(
    scenarios: list[str] | None = None,
    targets: list[str] | None = None,
    max_difficulty: str = "Hard",
) -> Any:  # pandas DataFrame
    """Return a filtered DataFrame of exercises from the exercise space."""
    # TODO: return ExerciseGenerator().filter(...)
    raise NotImplementedError


def generate_exercise(
    scenario: str | None = None,
    target: str | None = None,
    difficulty: str = "Medium",
    format: str = "Natural language text",
    n: int = 1,
) -> list[dict]:
    """
    Generate n new exercises.

    Each dict in the returned list has:
        id         : int
        scenario   : str
        difficulty : str
        text       : str  (natural language)
        known      : {symbol: value}
        target     : str
    """
    # TODO: return ExerciseGenerator().generate(...)
    raise NotImplementedError("Connect your exercise generator here.")

# ===========================================================================
# 5. Exercise Generation
# ===========================================================================
    
def gen_problem_with_values(problem_class='SingleStep', attributes={}, values={}):
    """Given a problemclass, attributes and values the ProblemGenerator is called to generate an exercise with the specification.
    - Attributes can be given as:
        attributes = [('12', 'is_adiabatic', True), ('12', 'is_isobaric', True)] 
        the tuple contains the id of the transition, the name of the attribute and the value. Attributes without a value are set to False
    - Values can be given as:
        values={'Q_12': 0, 'q_12': 0}
        the dictionary contains the variable id and the corresponding value.
    The given attributes might not be needed to compute the solution, at least one of the given values is used in the solution path.
    
    Returns generated problem (yaml), solution and solution path."""
    problem = GenerateProblem.ProblemGenerator(problem_class, attributes=attributes, values=values, only_template=False, print_solution=False)
    clean_dict(problem.problem_element)
    generated_problem = problem.problem_element
    generated_solution = problem.expected_solution
    generated_solution_path = problem.solution_path
    return generated_problem, generated_solution, generated_solution_path
    
    
def clean_dict(dict_to_clean):
    """Generates a new dict without (key, None) pairs."""
    remove_list = []
    for key, value in dict_to_clean.items():
        if isinstance(value, dict):
            if 'value' in value and value['value'] is None:
                remove_list.append(key)
            else:
                clean_dict(value)
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    clean_dict(item)
    for key in remove_list:
        del dict_to_clean[key]


def format_unit_display(unit: str | None) -> str:
    """Return a compact math-formatted unit label for Streamlit UI labels."""
    if unit is None:
        return ""

    unit_text = str(unit).strip()
    if not unit_text or unit_text.lower() in {"none", "null"}:
        return ""

    if unit_text.startswith("$") and unit_text.endswith("$"):
        unit_text = unit_text[1:-1].strip()

    unit_text = unit_text.strip("[]").strip()
    if "/" in unit_text and not unit_text.lstrip().startswith("\\frac"):
        left, right = [part.strip() for part in unit_text.split("/", 1)]
        if left and right:
            unit_text = rf"\frac{{{left}}}{{{right}}}"
    unit_text = latex_typsetting(unit_text)
    # return rf"$\left[{unit_text}\right]$"
    return rf"${unit_text}$"


def cyto_to_graphviz(cyto_elements: list, graph_colors: dict | None = None) -> graphviz.Digraph:
    """Convert cyto elements to a Graphviz digraph."""
    colors = graph_colors or {
        "required": "indianred1",
        "assignment": "palegreen1",
        "variable": "white",
        "equation": "silver",
        "rule": "steelblue2",
    }
    g = graphviz.Digraph()
    g.attr(rankdir="TB")
    for elem in cyto_elements:
        data = elem.get("data", {})
        if "source" in data and "target" in data:
            g.edge(data["source"], data["target"], label=data.get("label", ""))
            continue

        cls = elem.get("classes", "variable")
        shape = "ellipse" if cls in {"variable", "required", "assignment"} else "box"
        g.node(
            data.get("id", ""),
            label=data.get("label", data.get("id", "")),
            shape=shape,
            fillcolor=colors.get(cls, "white"),
            style="filled",
            fontsize="10",
        )
    return g


def cyto_to_agraph(cyto_elements: list) -> tuple[list[Node], list[Edge]]:
    """Convert cyto elements to streamlit-agraph node/edge lists."""
    node_colors = {
        "required": "#f28b82",
        "assignment": "#81c995",
        "variable": "#f1f3f4",
        "equation": "#c2e7ff",
        "rule": "#aecbfa",
    }
    nodes: list[Node] = []
    edges: list[Edge] = []

    for elem in cyto_elements:
        data = elem.get("data", {})
        if "source" in data and "target" in data:
            edges.append(
                Edge(
                    source=data["source"],
                    target=data["target"],
                    label=data.get("label", ""),
                    arrows="to",
                    smooth=False,
                )
            )
            continue

        cls = elem.get("classes", "variable")
        node_shape = "dot" if cls in {"variable", "required", "assignment"} else "box"
        nodes.append(
            Node(
                id=data.get("id", ""),
                label=data.get("label", data.get("id", "")),
                title=f"{cls}: {data.get('id', '')}",
                shape=node_shape,
                size=20 if node_shape == "dot" else 18,
                color=node_colors.get(cls, "#f1f3f4"),
            )
        )

    return nodes, edges


def filter_cyto_elements(
    cyto_elements: list,
    show_variables: bool,
    show_equations: bool,
    show_rules: bool,
) -> list:
    """Filter cyto elements by node class and keep only edges between visible nodes."""
    allowed_classes = set()
    if show_variables:
        allowed_classes.update({"variable", "required", "assignment"})
    if show_equations:
        allowed_classes.add("equation")
    if show_rules:
        allowed_classes.add("rule")

    visible_nodes = []
    visible_node_ids = set()

    for elem in cyto_elements:
        data = elem.get("data", {})
        if "source" in data and "target" in data:
            continue

        elem_class = elem.get("classes", "variable")
        if elem_class in allowed_classes:
            visible_nodes.append(elem)
            node_id = data.get("id")
            if node_id is not None:
                visible_node_ids.add(node_id)

    visible_edges = []
    for elem in cyto_elements:
        data = elem.get("data", {})
        if "source" not in data or "target" not in data:
            continue
        if data["source"] in visible_node_ids and data["target"] in visible_node_ids:
            visible_edges.append(elem)

    return visible_nodes + visible_edges