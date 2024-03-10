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

# Testing local

If you just need to test whether pip install works from the built package, you can create it and then use pip to install it from local filesystem.

```commandline
pip install dist/nmbrs-0.0.302.tar.gz
pip install dist/nmbrs-0.0.302-py3-none-any.whl
```

If you have been running python setup.py install already, ensure you run:
```commandline
pip uninstall nmbrs
```

to uninstall existing package first. You can encounter strange situations where mixing python setup.py install and pip locally, so run pip uninstall multiple times until says no more package to remove to be safe.
