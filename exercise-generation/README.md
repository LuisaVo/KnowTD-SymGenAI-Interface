# Exercise Generation
This project implements a **hybrid symbolic–neural pipeline** for generating *technically correct*, *pedagogically coherent*, and *textbook-style* thermodynamics exercises.  
It combines **formal logic (FO·)**, **IDP-Z3**, **KnowTD**, and **LLMs** to systematically enumerate valid problem scenarios and automatically produce complete exercises with solutions.

---

## Overview

Thermodynamics problems contain logical and physical constraints that are easy to violate when generated purely by machine learning.  
This project solves that problem using a **correct-by-construction pipeline** composed of two stages:

### 1. Formal Stage (Symbolic)

- FO(·) theory defines all allowed transition types, and physical constraints.
- IDP-Z3 performs **model expansion** to enumerate all distinct *valid* thermodynamic process configurations.
- KnowTD builds a **domain-complete knowledge graph** containing the variables, equations, and relations allowed for each configuration.

**Output:**  
- Set of all valid thermodynamic scenarios  
- A scenario-specific knowledge graph defining variables and equations  

**Example:**
You can checkout the domain models of the thermodynamics and geometry examples here:
- Thermodynamics: https://interactive-consultant.idp-z3.be/?gist=0f9912109847945b9dc2fcd756145072&file=Thermo_domain_model.idp
- Triangle-Geometry https://interactive-consultant.idp-z3.be/?gist=53fc5956146bf4be430c7c0652105d34&file=Triangle_example.idp

Either inspect the FO(·) model or click on `Interactive Consultant` to enter values of a structure. You can explore different combinations of attributes such as the `transition has type` and `transition has case` for thermodynamics and `Triangle has side type(s)` and `has angle type` for triangles.

---

### 2. Generative Stage (Neural-Assisted)

Given a scenario and its knowledge graph:

1. **Variable Selection**
   - Chooses given and required variables
   - Ensures all required variables are computable
   - Constructs a valid solution path (subgraph)

2. **Value Assignment**
   - Generates *plausible, physically consistent* numerical values
   - Computes all dependent state and transition properties using KnowTD

3. **Exercise Construction**
   - Builds a YAML-based abstract exercise representation
   - LLM transforms this into a human-readable thermodynamics problem
      - You can use the Prompt-Template (see Folder Gnerated Exercises) to translate the yaml into text. Replace <ADD YOUR YAML HERE> with your yaml.

**Output:**  
- A valid computation graph (solution path)  
- A complete YAML exercise  
- A final natural-language problem statement  
---

## Project Structure

```
exercise-generation/
├── Generated Exercises/
│   ├── Template.yaml                     # YAML template to describe a exercise manually.
│   ├── Prompt-Template.yaml                     # Prompt template to translate YAML into text.
|   ├── scenario_combinations.csv         # Description of all possible, valid scenarios
│   ├── HeatAndWork/                      # Exercises where Q ≠ 0 and W ≠ 0
│   ├── NoHeat/                           # Exercises where Q = 0
│   └── NoWork/                           # Exercises where W = 0
│
├── scripts/
│   ├── Thermodynamics-knowledgebase.idp  # Domain knowledge base
│   ├── model_expansion.py                # Model expansion to obtain all valid transition scenarios
│   ├── GenerateProblem.py                # Produces Knowledge Graph and selects given/required variables
│   ├── ExerciseGeneration.ipynb          # Enumerates valid transition combinations and generates YAML Exercises using GenerateProblem
│   └── ExerciseYamlToText.ipynb                # Transforms YAML exercises into textbook-style problems
│
├── README.md
└── requirements.txt
```

## Installation

```bash
git clone <your-repo-url>
cd <repo>
pip install -r requirements.txt
```

## Authors and acknowledgment- **Luisa Vollmer**  
- **Rebecca Loubet**  
- **Hans Hasse**
- **Daniel Neider**
- **Heike Leitte**  

We gratefully acknowledge the support by Deutsche Forschungsgemeinschaft DFG in the frame of the Priority Program 2331 ``Machine Learning in Chemical Engineering''.

## License
This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg