# Recommendation-system-

- Get Started

```
virtualenv env
.\env\Scripts\activate.ps1
pip install -r requirements.txt
```

- Hook install
```
pre-commit install
```

- Hook run command
```
pre-commit run --all-files
```

- Lint

```
pylint $(git ls-files '*.py')
flake8 $(git ls-files '*.py')
```

- Format
```
black .
```
