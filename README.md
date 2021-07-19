# Example Usage of the Data Repository with DVC and MLflow
This repository is a demonstration of a workflow for: 

a) Using the Data Repository using dvc

b) Creating a local tracking server with MLflow

c) Tracking experiments

d) Visualizing the experiments with the MLFlow UI

Two example projects at different stages are prepared.

After the general setup, go to the respective directory and follow the steps there.

## Setup

1. Clone the Github Repository
```bash
git clone git@github.com:VisiumCH/metrohm-dvc-demo-example.git
```

2. Install all requirements from requirements.txt
```bash
python3 -m pip install -r requirements.txt
```

Note 1: It's best to create a new python environment first.
Note 2: If you run into problems, try upgrading pip.

## Ressources
General information about MLflow experiment tracking: https://www.mlflow.org/docs/latest/tracking.html

Logging parameters with tensorflow: https://www.mlflow.org/docs/latest/tracking.html
