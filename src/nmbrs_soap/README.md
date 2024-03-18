# Visma-NMBRS-SOAP-API-SDK

***

Python SDK for the Visma Nmbrs SOAP API. Simplifying integration and enhancing developer productivity.


# Installation

***

To install this packages run:

```shell
pip install nmbrs_soap_api
```

# Getting started

***

This (SDK)Software development Kit uses the **Nmbrs Soap API** to access nmbrs.

There is also a **Rest API** available but this is not included in this SDK.

For more info on the Soap api go [here](https://support.nmbrs.nl/hc/nl/articles/205903718-Nmbrs-API-for-developers#topic_basics).

TO read about the rest api here is a good [source to get started](https://developer.nmbrs.com/docs).

In case of dificultis in developing anything nmbrs related contact:
- [Rene Dijkgraaf](https://www.linkedin.com/in/ren%C3%A9-dijkgraaf-226b9b2a/)
- [Wilko Kluijtmans](https://www.linkedin.com/in/wilko-kluijtmans-5437b3122/)
- [Lars Kluijtmans](https://www.linkedin.com/in/lars-kluijtmans-aa4a10243/)
- [Incomme](https://www.incomme.nl/)

## Authentication

***

There are two authentication options build into the SDk:

1. Using the username and token
2. Using the username, token and domain

When only using the username and token the call [**DebtorService:Environment_Get**](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Environment_Get) will be used to retrieve the domain from nmbrs. Seeing as this call is only available on the debtor level, you might not want to activate it for your users or cant at all.

In this case use option 2, here you specify the domain yourself, but this way the validity of your credentials(username, token and domain) is never verified.

### Getting the nmbrs token

Retrieving a nmbrs api token can be done through the nmbrs website, as shown [here](https://support.nmbrs.com/hc/en-us/articles/360013305712-How-to-get-an-API-token).

Managing api access cen be done using the User Templates, as shown [here](https://support.nmbrs.com/hc/en-us/articles/360013527371-API-User-Template).

### Initialize SDK using username and token

***

```python
from nmbrs import Nmbrs

api = Nmbrs(username="__username__", token="__token__", auth_type="token")

print(api.debtor_service.auth_header)
```

The created credentials are saved in the SDK for later use.

If not all needed parameters are specified an MissingParams exception will the thrown.

### Initialize SDK using username, token and domain

***

```python
from nmbrs import Nmbrs

api = Nmbrs(username="__username__", token="__token__", domain="__domain__", auth_type="with domain")

print(api.debtor_service.auth_header)
```

The created credentials are saved in the SDK for later use.

**Note:** these credentials are not authenticated and may not be valid.

## Testing environment: Sandbox

For testing Nmbrs provides a Sandbox feature. To read more about the sandbox, its usages and limitations go [here](https://support.nmbrs.nl/hc/nl/articles/204054506-Sandbox).

By default, the SDK uses the sandbox instead of the live environment, this is done to prevent accidental modifying of data in the live environment.

To access the live environment you can use the following code:

```python
from nmbrs import Nmbrs

api = Nmbrs(sandbox=False)

print(api.sandbox)
```

**Note:** the usage of the sandbox is set when the SDK is initialized and can not be modified after.

## Retrieving data

Now that you have set up the needed authentication its possible to retrieve data from nmbrs.

The nmbrs Soap API, and by extension this SDK, are split into 5 services:

- [Debtor service](https://api.nmbrs.nl/soap/v3/DebtorService.asmx)
- [Company service](https://api.nmbrs.nl/soap/v3/CompanyService.asmx)
- [Employee service](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx)
- [Single Sign-on service](https://api.nmbrs.nl/soap/v3/SingleSignOn.asmx)
- [Report service](https://api.nmbrs.nl/soap/v3/ReportService.asmx)

**Note:** the **Report service** is not yet included into this SDK.

```python
from nmbrs import Nmbrs

api = Nmbrs(username="__username__", token="__token__", auth_type="token")

debtors = api.debtor.get_all()

print(len(debtors.to_dict()))
```

Each object returned has a to_dict() function that reruns the object in the form of a dictionary. 

## Exception handling

In case a user does not have access to the needed endpoints an AuthorizationError will be raised.

To handle these Exceptions you can take inspiration from the following code.

```python
from nmbrs import Nmbrs
from nmbrs.exceptions import AuthorizationError

api = Nmbrs(username="__username__", token="__token__", auth_type="token")

try:
    debtors = api.debtor.get_all()
except AuthorizationError as e:
    print(f"User does not have access to: {', '.join(e.resources)}'")
```

## Single Sign-on(SSO)

When it comes to Nmbrs Single Sign-On service:

 - Username and Token
 - Username and Password
 - Username, Password and Domain

SSO Flow:

- First get a sso token that is valid for 30 seconds.
- This token can be used to creat an url that automatically sign the user into Nmbrs.

For details on how to implement the entire SSO Flow go [here](https://support.nmbrs.com/hc/en-us/articles/360013311952-Single-Sign-On-Service-Flow-SSO).

### SSO Token:

#### Username and Token

```python
from nmbrs import SingleSingOnService

sso_service = SingleSingOnService()

sso_token = sso_service.sso_auth_with_token("__username__", "__token__")

print(sso_token)
```

#### Username and Password

```python
from nmbrs import SingleSingOnService

sso_service = SingleSingOnService()


sso_token = sso_service.sso_auth_with_password("__username__", "__token__")

print(sso_token)
```

**Note:** this function will raise an exception if you have accounts in multiple Nmbrs environments. In this case use the following call where you specify the domain you want to log in to. 

#### Username, password, and domain

```python
from nmbrs import SingleSingOnService

sso_service = SingleSingOnService()


sso_token = sso_service.sso_auth_with_domain("__username__", "__password__", "__domain__")

print(sso_token)
```

### SSO url:

Using the token reverence from the aforementioned functions we can create an url that automatically refers the user to nmbrs.

```python
from nmbrs import SingleSingOnService

sso_service = SingleSingOnService()

sso_token = sso_service.sso_auth_with_password("__username__", "__password__")
sso_url = sso_service.get_sso_url(sso_token, "__domain__")

print(sso_url)
```
