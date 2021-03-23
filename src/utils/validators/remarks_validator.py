""" file to have class with payment remarks validation """
from abc import ABC

from utils.constants import PolicyCodes
from utils.validators.base_validator import BaseValidator, ValidationMessage

from utils.policy_request import PolicyRequest


class PaymentRemarksValidator( BaseValidator, ABC ):
    """ class to validate customer payment remarks """
    def __init__(self, customer_remarks: PolicyRequest,
                 criteria_12m: int, criteria_remarks: int):
        self.customer_remarks = customer_remarks
        self.criteria_12m = criteria_12m
        self.criteria_remarks = criteria_remarks

    def is_valid(self) -> ValidationMessage:
        """ override method to perform payment remarks validation """
        status = True
        code = PolicyCodes.ACCEPT
        if self.customer_remarks.remarks_12m > self.criteria_12m:
            status = False
            code = PolicyCodes.PAYMENT_REMARKS_12M
            #  return and do not  check further
            return ValidationMessage( status, code.name )

        if self.customer_remarks.remarks > self.criteria_remarks:
            status = False
            code = PolicyCodes.PAYMENT_REMARKS

        return ValidationMessage( status, code.name )
