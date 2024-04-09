"""Base for nmbrs errors"""

from ...__version__ import __git_issues__


class NmbrsBaseException(Exception):
    """
    Base for nmbrs errors

    For more details on Nmbrs API error codes, refer to:
        - [Nmbrs API Error Codes](https://support.nmbrs.com/hc/en-us/articles/360013526891-Nmbrs-API-error-codes)
        - [API Invalid Authentication](https://support.nmbrs.com/hc/en-us/articles/360015628919-API-error-1001-Invalid-Authentication)
        - [API User Template](https://support.nmbrs.com/hc/en-us/articles/360013527371-API-User-Template)
    """

    def __init__(self, error_code: int, resource: str):
        self.error_code = error_code
        self.resource = resource

        self.title = ""
        self.cause = ""
        self.solution = ""

        self.get_error()

        self.message = f"Error: {self.title}\n" f"  Resource: {self.resource}\n" f"  Cause: {self.cause}\n" f"  Solution: {self.solution}\n"
        super(Exception, self).__init__(self.message)

    def get_error(self):
        """Get the name, cause and solution of an exception."""
        match self.error_code:
            case 1000:
                self.title = "Invalid combination email/password"
                self.cause = "Invalid combination email/password"
                self.solution = "Make sure that the email and the password that you use are right"
            case 1001:
                self.title = "Invalid Authentication"
                self.cause = "The email address, API token or domain is not valid."
                self.solution = (
                    "Make sure that the email and the token that you use are right. For more information see"
                    " [API Invalid Authentication](https://support.nmbrs.com/hc/en-us/articles/360015628919-API-"
                    "error-1001-Invalid-Authentication)"
                )
            case 1002:
                self.title = "Unauthorized Access"
                self.cause = "You do not have the rights for the debtor, company or the employee services. "
                self.solution = (
                    "Contact the administrator of the environment and review the API template. See"
                    " [API User Template](https://support.nmbrs.com/hc/en-us/articles/360013527371-API-User-Template)"
                )
            case 1003:
                self.title = "Unauthorized Access Data"
                self.cause = "You do not have the rights for the debtor or company."
                self.solution = "Contact the administrator of the environment and review access rights by tags/filters."
            case 1004:
                self.title = "Disabled, no valid subscription"
                self.cause = "Disabled, no valid subscription"
                self.solution = ""
            case 1006:
                self.title = "Generic Login Security Failure"
                self.cause = "Unknown"
                self.solution = "Retrying tends to solve the issue."
            case 2001:
                self.title = "Invalid Hour component"
                self.cause = "Hour component number is not right. Hour component is not inserted."
                self.solution = (
                    "Use valid hour component number. To see the hour components that are in use see method HourModel_GetHourCodes."
                )
            case 2002:
                self.title = "Invalid Wage Component"
                self.cause = "Wage component number is incorrect, therefore the wage component is not inserted."
                self.solution = (
                    "Insert a valid wage component number. To see the wage components that are in use, "
                    "see method WageModel_GetWageCodes."
                )
            case 2003:
                self.title = "Unauthorized Access"
                self.cause = "You do not have the rights to the employee that you are using the API method for."
                self.solution = "Make sure you have the correct EmployeeID."
            case 2004:
                self.title = "Unauthorized Access"
                self.cause = "You do not have the rights to the company that you are using the API method for."
                self.solution = "Make sure you have the correct CompanyID."
            case 2006:
                self.title = "Invalid Period"
                self.cause = "Inserted period is not according to the company's period type."
                self.solution = "Use the period type according to company settings."
            case 2009:
                self.title = "Unauthorized Access"
                self.cause = "You do not have the rights to the debtor that you are using the API method for."
                self.solution = "Make sure you have the correct DebtorId."
            case 2011:
                self.title = "Protected Mode: Cannot Change in the Past"
                self.cause = "You are changing something in the past or future without unprotected mode on."
                self.solution = "You need to put the unprotected mode on by filling <UnprotectedMode>boolean</UnprotectedMode> with true."
            case 2012:
                self.title = "Wage Tax Declaration Already Sent"
                self.cause = "Wage tax declaration already sent"
                self.solution = ""
            case 2013:
                self.title = "Operation Not Possible On Free Trial"
                self.cause = "Operation not possible on free trial"
                self.solution = "Update your account from the free trial. See this list of enumerations."
            case 2014:
                self.title = "Invalid BankAccount IBAN"
                self.cause = "Invalid BankAccount IBAN"
                self.solution = "Insert a valid bank account IBAN."
            case 2015:
                self.title = "Invalid BankAccount Number"
                self.cause = "Invalid BankAccount Number"
                self.solution = "Insert a valid bank account number."
            case 2016:
                self.title = "Invalid BankAccount Type"
                self.cause = "Invalid BankAccount Type"
                self.solution = "Insert a valid bank account type. See the BankAccountType enumeration for valid values."
            case 2017:
                self.title = "Invalid Labour Agreement ID"
                self.cause = "Invalid Labour Agreement ID"
                self.solution = (
                    "Insert a valid Labour Agreement ID. You may get them using the methods LabourAgreements_Get "
                    "and LabourAgreements_GetCurrent."
                )
            case 2018:
                self.title = "Invalid Leave ID"
                self.cause = "Invalid Leave ID"
                self.solution = "Insert a valid Leave ID. You can get the available Leave IDs with the method Leave_GetList_V2."
            case 2019:
                self.title = "Task Status Not Available"
                self.cause = "Possibly caused by an error or the task ID belongs to a different task."
                self.solution = "Insert a valid task ID or retry launching the task."
            case 2020:
                self.title = "Task Status Not Available"
                self.cause = "Possibly caused by an error or the task ID belongs to a different task."
                self.solution = "Insert a valid task ID or retry launching the task."
            case 2021:
                self.title = "Invalid Task Result"
                self.cause = "Task doesn’t have the correct format or the task ID used belongs to a different task."
                self.solution = "Insert a valid task ID or retry launching a task."
            case 2022:
                self.title = "Invalid Leave Type"
                self.cause = "Invalid Leave Type or the leave type requested isn’t available."
                self.solution = "Insert a valid leave type from the enumeration."
            case 2028:
                self.title = "Start Time Cannot Be After End Time"
                self.cause = "The start time must always be before the end time"
                self.solution = "Make sure the end time is not before the start time"
            case 2029:
                self.title = "Time Slots Cannot Overlap"
                self.cause = "Time Schedule in SE cannot have overlapping slots"
                self.solution = "Check what are the current time slots and make sure what you are trying to add is not overlapping"
            case 2030:
                self.title = "Invalid Set of Values"
                self.cause = "The values inputted are invalid"
                self.solution = (
                    "Review if you are not inserting any type of value incorrectly. For example, characters where it's expected int."
                )
            case 2032:
                self.title = "Bank Account IBAN Required"
                self.cause = "The IBAN was not given in the input"
                self.solution = "Add the IBAN to the input."
            case 2033:
                self.title = "Tax Type Required"
                self.cause = "SE-only. The tax type was not inputted."
                self.solution = "Add a tax type to the input."
            case 2034:
                self.title = "Invalid Tax Type"
                self.cause = "SE-only. The tax type is invalid."
                self.solution = "Add a valid tax type to the input."
            case 2035:
                self.title = "Tax Form Required"
                self.cause = "SE-only. The tax form for was not inputted."
                self.solution = "Add a tax form to the input."
            case 2036:
                self.title = "Invalid Tax Form"
                self.cause = "SE-only. The tax form is invalid."
                self.solution = "Add a valid tax form to the input."
            case 2037:
                self.title = "Invalid CostCenterId"
                self.cause = "The CostCenterId inputted is invalid"
                self.solution = "Get the list of valid cost centers and try again."
            case 2038:
                self.title = "Invalid CostCenterCode"
                self.cause = "The CostCenterCode inputted is invalid"
                self.solution = "Get the list of valid cost centers and try again."
            case 2039:
                self.title = "Duplicated Cost Center Code"
                self.cause = "The cost center code is duplicated and that's not allowed"
                self.solution = "Only one cost center can be added at a time."
            case 2040:
                self.title = "Provide File Name with an Extension"
                self.cause = "The file added was not inputted with an extension"
                self.solution = "It's mandatory to add the extension of the file when uploading. Please try again with the extension."
            case 2041:
                self.title = "File Too Large"
                self.cause = "File is too big to be uploaded"
                self.solution = "Try uploading the file again in a smaller size."
            case 2042:
                self.title = "User Belongs to Multiple Environments, Cannot SSO"
                self.cause = "This username belongs to multiple environments, it could not be authenticated."
                self.solution = "Use the call GetTokenWithDomain instead of GetToken to authenticate and SSO."
            case 2043:
                self.title = "Invalid Domain"
                self.cause = "An invalid domain was inputted"
                self.solution = "Add a valid domain."
            case 2044:
                self.title = "Invalid Endpoint"
                self.cause = "Endpoint does not have a valid format"
                self.solution = "Add an endpoint with a valid format, with 'https://' on the URL."
            case 2045:
                self.title = "Invalid Name"
                self.cause = "Name cannot be empty, it's a mandatory field"
                self.solution = "Add a name for this webhook setting."
            case 2046:
                self.title = "Not Found"
                self.cause = "Could not find the requested resource"
                self.solution = "Input a valid resource, use a GET call to retrieve the data."
            case 9999:
                self.unknown_error()
                self.title = "Unkown"  # Actual title returned by nmbrs
            case _:
                self.unknown_error()

    def unknown_error(self):
        """Unknown error, No documentation found"""
        self.title = "Unknown Nmbrs error"
        self.cause = "Unknown"
        self.solution = f"Create a issue on our git page: {__git_issues__}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.message})"
