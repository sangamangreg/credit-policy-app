""" file to have class with payment remarks validation """
from abc import ABC

from utils.constants import PolicyCodes
from utils.validators.base_validator import BaseValidator, ValidationMessage


class PaymentRemarksValidator( BaseValidator, ABC ):
    """ class to validate customer payment remarks """
    def __init__(self, remarks: int, criteria_remarks: int):
        self.remarks = remarks
        self.criteria_remarks = criteria_remarks

    def is_valid(self) -> ValidationMessage:
        """ override method to perform payment remarks validation """
        status = True
        code = PolicyCodes.ACCEPT

        if self.remarks > self.criteria_remarks:
            status = False
            code = PolicyCodes.PAYMENT_REMARKS

        return ValidationMessage( status, code.name )


class PaymentRemarks12MValidator( BaseValidator, ABC ):
    """ class to validate customer payment remarks 12m """
    def __init__(self, remarks_12m: int, criteria_12m: int):
        self.remarks_12m = remarks_12m
        self.criteria_12m = criteria_12m

    def is_valid(self) -> ValidationMessage:
        """ override method to perform payment remarks 12m validation """
        status = True
        code = PolicyCodes.ACCEPT
        if self.remarks_12m > self.criteria_12m:
            status = False
            code = PolicyCodes.PAYMENT_REMARKS_12M

        return ValidationMessage( status, code.name )
