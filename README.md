# Nmbrs SDK

---

Python SDK for the Visma Nmbrs SOAP API. Simplifying integration and enhancing
developer productivity.

## Installation

---

To install this package, run:

```shell
pip install nmbrs
```

## Getting started

---

This Software Development Kit (SDK) facilitates interaction with the Nmbrs SOAP
API.

Please note that this SDK specifically targets the Nmbrs SOAP API.

Although there is also a Rest API available, it is not covered in this SDK.

For more information on the SOAP API, refer to the
[NMBRS SOAP API documentation](https://support.nmbrs.nl/hc/nl/articles/205903718-Nmbrs-API-for-developers#topic_basics).

To explore the Rest API, you can refer to the
[NMBRS REST API documentation](https://developer.nmbrs.com/docs).

If you encounter any difficulties or have questions related to development with
Nmbrs, feel free to reach out to:

- [Lars Kluijtmans](https://www.linkedin.com/in/lars-kluijtmans-aa4a10243/)
- [Rene Dijkgraaf](https://www.linkedin.com/in/ren%C3%A9-dijkgraaf-226b9b2a/)
- [Wilko Kluijtmans](https://www.linkedin.com/in/wilko-kluijtmans-5437b3122/)

These contacts can provide assistance and support for your Nmbrs-related
development endeavors.

## Authentication

---

There are two authentication options built into the SDK:

1. Using the username and token
2. Using the username, token, and domain

When using only the username and token, the call
[**DebtorService:Environment_Get**](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Environment_Get)
will be made to retrieve the domain from Nmbrs.

In the second option, you specify the domain yourself, but the validity of your
credentials (username, token, and domain) is not verified.

## Getting the Nmbrs Token

---

You can retrieve a Nmbrs API token through the Nmbrs website.
For detailed instructions, refer to [How to get an API token](https://support.nmbrs.com/hc/en-us/articles/360013305712-How-to-get-an-API-token).

API access management can be handled using User Templates. Learn more about this
feature [here](https://support.nmbrs.com/hc/en-us/articles/360013527371-API-User-Template).

## Initialize SDK Using Username and Token

---

Default authentication flow, using the username and token to retrieve the domain
name, this automatically validates the credentails.

```python
from nmbrs import Nmbrs

api = Nmbrs(username="__username__", token="__token__")

print(api.debtor.auth_manager.get_username())
```

The provided credentials are saved in the SDK for later use.
If not all required parameters are specified, a MissingParams exception will be
thrown.

## Initialize SDK Using Username, Token, and Domain

---

In the following authentication methode all needed authentication credentials
are passed in, but these will not be validated.

```python
from nmbrs import Nmbrs

api = Nmbrs(username="__username__", token="__token__", domain="__domain__", auth_type="domain")

print(api.debtor.auth_manager.get_username())
```

The provided credentials are saved in the SDK for later use.

Please note that these credentials are not authenticated and may not be valid.

## Testing Environment: Sandbox

---

For testing purposes, Nmbrs provides a Sandbox feature. To learn more about the
sandbox, its usage, and limitations, refer to the [Sandbox documentation](https://support.nmbrs.nl/hc/nl/articles/204054506-Sandbox).

By default, the SDK uses the sandbox instead of the live environment to prevent
accidental modification of data in the live environment.

To access the live environment, use the following code:

```python
from nmbrs import Nmbrs

api = Nmbrs(username="__username__", token="__token__", sandbox=False)
```

Please note that the usage of the sandbox is set when the SDK is initialized
and cannot be modified afterward.

## Retrieving Data

---

Now that you have set up the necessary authentication, it's possible to retrieve
data from Nmbrs.

The Nmbrs SOAP API, and by extension this SDK, are split into 5 services:

- [Debtor service](https://api.nmbrs.nl/soap/v3/DebtorService.asmx)
- [Company service](https://api.nmbrs.nl/soap/v3/CompanyService.asmx)
- [Employee service](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx)
- [Single Sign-on service](https://api.nmbrs.nl/soap/v3/SingleSignOn.asmx)
- [Report service](https://api.nmbrs.nl/soap/v3/ReportService.asmx)

You can access data from Nmbrs using the various services available. For example:

```python
from nmbrs import Nmbrs

api = Nmbrs(username="__username__", token="__token__")

# Retrieve all debtors
debtors = api.debtor.get_all()

# Print the number of debtors
print(len(debtors))

# Print the details of the first debtor as a dictionary
print(debtors[0].to_dict())
```

Each object returned has a to_dict() function that returns the object in the
form of a dictionary.

Additionally, you can use the serialize function to convert objects, lists of
objects, etc., into dictionaries:

```python
from nmbrs import Nmbrs, serialize

api = Nmbrs(username="__username__", token="__token__")

debtors = api.debtor.get_all()

print(serialize(debtors))
```

This allows for easy manipulation and transformation of data returned from the
Nmbrs API.

### Error Handling

---

The Nmbrs SDK provides robust error handling mechanisms to assist developers
in diagnosing and resolving issues encountered during API interaction.
This section outlines the various types of exceptions that may be raised and
how to handle them effectively.

### Nmbrs Base Exception

The base Nmbrs exception, NmbrsBaseException, serves as the foundation for
specific error types within the SDK.

It contains the following attributes:

- error_code: The error code associated with the exception.
- resource: The name of the endpoint associated that caused the error.
- title: A title summarizing the error.
- cause: Describes the cause of the error.
- solution: Provides a suggested solution or action to resolve the error.

### Handling Exceptions

To handle exceptions gracefully, use Python's try-except block.

Nmbrs exceptions consist of:

- error_code: The error code of the specified error returned.
- resource: The endpoint that caused the exception to occur.
- title: Short description of the error.
- cause: Possible cause as indicated by Nmbrs.
- solution: Recommended solution from nmbrs.

#### Nmbrs base exception

If you want to handle all the Nmbrs exceptions the same way use the NmbrsBaseException:

```python
from nmbrs import Nmbrs
from nmbrs.exceptions import NmbrsBaseException

try:
    api = Nmbrs(username="__username__", token="__token__")
except NmbrsBaseException as e:
    print(f"Nmbrs error: {e.resource}")
```

#### Specific Nmbrs exceptions

You can catch specific exceptions and handle them accordingly based on the error
scenario.

Here's an example:

```python
from nmbrs import Nmbrs
from nmbrs.exceptions import AuthenticationException, AuthorizationException

try:
    api = Nmbrs(username="__username__", token="__token__")
except AuthenticationException as e:
    print(f"Authentication error: {e.resource}")
except AuthorizationException as e:
    print(f"Authorization error: {e.resource}")
```

By catching and handling exceptions, you can provide meaningful feedback to
users and take appropriate actions to address errors encountered during API
interactions.

## Report service

The Report service allows you to interact with report-related functionality
provided by Nmbrs SOAP API.
Please note that not all specific calls in the report service are implemented
in this SDK.

To utilize the available functionality, you need to consult the
[Nmbrs documentation](https://api.nmbrs.nl/soap/v3/ReportService.asmx)
and provide the necessary parameters.

### Getting Started

To begin using the Report service, you first need to initialize an instance of
the Nmbrs SDK with your authentication details:

```python
from nmbrs import Nmbrs

api = Nmbrs(username="__username__", token="__token__")
```

### Example Usage

#### Retrieving Report Task ID

You can retrieve the task ID (GUID) for a specific report task by providing the
task name and parameters:

```python
task_name = "Reports_Accountant_CompanyContactPerson_Background"
task_parameters = {}

report_guid = api.report.get_task_id(task_name, task_parameters)
```

Once you have the GUID, Nmbrs will start generating the report in the background.

#### Requesting Report

You can request the generated report using the background_task_result call.
Specify the maximum amount of time you are willing to wait for the report to
be generated (in seconds):

```python
report_guid = "__your_guid__"

report = api.report.background_task_result(report_guid, 360)
```

#### Error Handling Background tasks

When requesting the report, Nmbrs may return errors. In such cases, the
following exceptions can be raised:

- **UnknownBackgroundTaskException**: Raised when the background task is unknown.
- **BackgroundTaskException**: Raised for general background task errors.

You can handle these exceptions as follows:

```python
from nmbrs.exceptions import (
    UnknownBackgroundTaskException,
    BackgroundTaskException,
)

report_guid = "__your_guid__"

try:
   report = api.report.background_task_result(report_guid, 360)
except UnknownBackgroundTaskException as e:
    print(e)
except BackgroundTaskException as e:
    print(e)
```

Ensure to handle these exceptions to provide appropriate error handling in your
application.

## Single Sign-on (SSO)

When it comes to the Nmbrs Single Sign-On service, authentication can be
achieved through various methods:

- Using Username and Token
- Using Username and Password
- Using Username, Password, and Domain

When it comes to Nmbrs Single Sign-On service:

- Username and Token
- Username and Password
- Username, Password and Domain

### SSO Flow

The Single Sign-On (SSO) flow involves the following steps:

1. Obtain an SSO token, which is valid for 30 seconds.
2. Use this token to generate a URL that automatically signs the user into
   Nmbrs.

For detailed implementation instructions on the entire SSO flow, refer to the
[Single Sign-On Service Flow (SSO) documentation](https://support.nmbrs.com/hc/en-us/articles/360013311952-Single-Sign-On-Service-Flow-SSO).

### SSO Token

#### Username and Token

```python
from nmbrs import SingleSingOnService

sso_service = SingleSingOnService()

sso_token = sso_service.get_token_with_api_token("__username__", "__token__")

print(sso_token)
```

#### Username and Password

```python
sso_token = sso_service.get_token_with_password("__username__", "__password__")

print(sso_token)
```

**Note**: This function will raise an exception if you have accounts in
multiple Nmbrs environments. In such cases, use the following call where you
specify the domain you want to log in to.

#### Username, password, and domain

```python
sso_token = sso_service.get_token_with_domain("__username__", "__password__", "__domain__")

print(sso_token)
```

#### SSO url

Using the token obtained from the aforementioned functions, you can create a
URL that automatically redirects the user to Nmbrs.

```python
sso_token = sso_service.get_token_with_password("__username__", "__password__")
sso_url = sso_service.get_sso_url(sso_token, "__domain__")

print(sso_url)
```

This URL simplifies the user authentication process and provides a seamless
login experience for Nmbrs users.
