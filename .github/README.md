# Workflows

## Unit tests

```commandline
coverage run -m pytest tests/
coverage html
```

## Linting

```commandline
pylint --rcfile=.pylintrc $(git ls-files '*.py')
pymarkdown scan $(git ls-files '*.md')
yamllint .
```

## Formatting

```commandline
black --check $(git ls-files '*.py')
prettier --check '**/*.md'
prettier --check '**/*.yml'
```
