# Tests

## Run tests locally

```commandline
coverage run -m pytest --cov=src/nmbrs tests/
```

## Generate report

```commandline
coverage run -m pytest tests/
coverage html
```

## Linting

```commandline
pylint --rcfile=.pylintrc $(git ls-files '*.py')
```
