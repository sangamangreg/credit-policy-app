""" a file to hold all constants and enums """
import enum


class PolicyCodes( enum.Enum ):
    """ Policy acceptance and rejection codes """

    ACCEPT = 1
    LOW_INCOME = 2
    HIGH_DEBT_FOR_INCOME = 3
    PAYMENT_REMARKS_12M = 4
    PAYMENT_REMARKS = 5
    UNDERAGE = 6


class PolicyCriteria:
    """
    Default criteria for policy acceptance. Keeping it at one place so that
    can change from one place whenever wants to update
    """

    INCOME = 500
    DEBT = 50
    AGE = 18
    remarks_12m = 0
    remarks = 1
