# Tests

## Run tests locally

```commandline
coverage run -m pytest --cov=src/nmbrs tests/test_nmbrs/
```

## Generate report

```commandline
coverage html
```

## Linting

```commandline
pylint --rcfile=.pylintrc $(git ls-files '*.py')
```
