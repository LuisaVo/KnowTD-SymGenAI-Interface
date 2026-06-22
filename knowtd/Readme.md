# Protoype for KnowTD
KnowTD is a knowledge graph of thermodynamics. It stores thermodynamic knowledge about concepts, equations and variables and can be used to solve thermodynamic problems.

## Demo
You can try out KnowTD here: https://knowtd.onrender.com/ or install and run it locally.
Note that the server will spin down with inactivity, which can delay requests by 50 seconds or more.

## Installation
- Install anaconda: https://www.anaconda.com/download
- Open a command line here
- Install the conda environment by running:
    `conda env create -f environment-setup.yml`

## How to start the inferface
- Open a command line here
- Activate the environment by runnning:
    `conda activate knowTD`
- Start the interface:
    `pyhton scripts/app.py`
- Follow the link in the command line to view the interface in the browser
- keep the comand line open, close it when you want to shut down the interface.

Here is a short video explaining the interface:

[![KnowTD Interface Tutorial](https://img.youtube.com/vi/0JOkZ2TdxXg/0.jpg)](https://youtu.be/0JOkZ2TdxXg)


## How to use KnowTD with a YAML File
- you can validate your yaml file and inferr missing elements using:
  `linkml-convert --infer -s ontology/thermodynamics_ontology.yaml -o problem_inferred.yaml --target-class Problem ~path/to/yourYAMLFile`
- or alternatively use this to validate the file (adjust the target class to be as precise as possible)
 `linkml-validate --target-class SingleStep --schema ontology/thermodynamics_ontology.yaml ~path/to/yourYAMLFile`
- run `python scripts/KnowTD_from_yaml_file.py`
- adjust the variable "problem_filename" to point to your yaml file.
- the script gives you feedback about the yaml import and about the reasoning in KnowTD. You can see the numerical values and the solution graph.

## How to run all unittests
`pyhton -m unittest`

## Evaluation
The testset is used to procude answers by KnowTD. They are incorporated in the interface and can also be tested using the YAML files. Furthermore, we used this testset also to test large language models, more information can be found here: https://gitlab.rhrk.uni-kl.de/knowtd/llm-benchmark-testsets

## Acknoledgements
We gratefully acknowledge the support by Deutsche Forschungsgemeinschaft DFG in the frame of the Priority Program 2331 ``Machine Learning in Chemical Engineering''.

## References
Parts of this work are published at the Journal of Chemical Information and Modeling https://doi.org/10.1021/acs.jcim.4c00647. This publication cover the ability to model thermodynamics theory in an ontology.

The solver strategy and it's application for explainable AI is published at the ESWC 2025 1st International Workshop on eXplainable AI and Knowledge Graphs https://ceur-ws.org/Vol-3977/XAIKG-3.pdf


## License
This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg