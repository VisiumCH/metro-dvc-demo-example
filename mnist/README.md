# Instructions
No DVC project has been imported to this project yet. Therefore the first step has to be to import the required data.

1. Add data to the git repository
```bash
dvc import git@github.com:VisiumCH/metro-dvc-demo.git images/my_mnist
```

2. Train the model
```bash
python mnist.py
```

3. Start MLFlow
```bash
mlflow ui
```

4. Keep on creating new runs and vary the parameters, and explore the UI.
