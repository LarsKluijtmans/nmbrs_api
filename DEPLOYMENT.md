# Deployment

Guide for the deployment of the application to pypi and TestPypi.

## Install packages

Install the needed packages **build** and **twine**.

```commandline
py -m pip install --upgrade build twine
```

## Create build

Create the files that will be used as the package.

```commandline
py -m build
```

## Deployment

### Test

To deploy the packages to the testing env use:

```commandline
py -m twine upload --repository testpypi dist/*
```


### Production

When pushing to production:

```commandline
py -m twine upload --repository pypi dist/*
```