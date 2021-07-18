# Example Usage of the Data Repository with DVC and MLflow
This repository is a demonstration of a workflow for: 

a) Using the Data Repository using dvc

b) Creating a local tracking server with MLflow

c) Tracking experiments

d) Visualizing the experiments with the MLFlow UI

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

3. Initialize the DVC project
```bash
dvc init
```

Note: You're dvc project might already be initialized.

4. Import the required dataset
```bash
dvc import git@github.com:VisiumCH/metro-dvc-demo.git images/augmented_mnist
```

5. Run the experiment
```bash
python3 augmented_my_mnist/mnist.py
```

6. Start the MLflow UI
```bash
mlflow ui
```

7. Keep on creating new runs and vary the parameters, and explore the UI.

## Ressources
General information about MLflow experiment tracking: https://www.mlflow.org/docs/latest/tracking.html

Logging parameters with tensorflow: https://www.mlflow.org/docs/latest/tracking.html
