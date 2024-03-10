# Tests

## Run tests

```commandline
pytest --cov=nmbrs tests/
```

## Linting

```commandline
pylint --rcfile=.pylintrc $(git ls-files '*.py')
```
