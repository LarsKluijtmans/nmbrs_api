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

Python

```commandline
pylint --rcfile=.pylintrc $(git ls-files '*.py')
```

Markdown

```commandline
prettier --check '**/*.md'
prettier --write '**/*.md'
```

## Formatting

Python

```commandline
black --check .
black .
```

Markdown

```commandline
pymarkdown scan "**/*.md"
```
