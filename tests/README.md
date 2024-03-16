# Tests

## Run tests locally

```commandline
coverage run -m pytest tests/
```

## Generate report

```commandline
coverage html
```

## Linting

```commandline
pylint --rcfile=.pylintrc $(git ls-files '*.py')
```
