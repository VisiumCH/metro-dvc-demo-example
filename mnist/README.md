# MNIST

# Import data
Add data to the git repository
```bash
dvc import git@github.com:VisiumCH/metro-dvc-demo.git images/my_mnist
```

# Training
```bash
python mnist.py
```

# Start MLFlow

```bash
mlflow ui
```