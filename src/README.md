### Create UML class diagram

create the uml class diagram for the nmbrs package.

- 1 Install the nmbrs package

```commandline
pip install nmbrs
```

Generate the uml diagram as a png

```commandline
pyreverse -o png -ASmy -c nmbrs.api.Nmbrs nmbrs
```
