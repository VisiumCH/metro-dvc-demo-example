# Instructions
The dvc project has already been initialized and imported. You can see this as the file _augmented_mnist.dvc_ is already present. Furthermore, there is a _dvc.yaml_ file within which pipelines have been defined.

1. Update the data:
```bash
dvc pull
```

2. Run the training:
```bash
dvc repro  # Trains the model as defined in dvc.yaml file.
```

3. Start the MLflow UI
```bash
mlflow ui
```

4. Keep on creating new runs and vary the parameters, and explore the UI.
