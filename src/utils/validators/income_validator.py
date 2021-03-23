""" file to have class with income validation """
from abc import ABC

from utils.constants import PolicyCodes
from utils.validators.base_validator import BaseValidator, ValidationMessage


class IncomeValidator( BaseValidator, ABC ):
    """ class to validate customer income """
    def __init__(self, income: float, income_criteria: float):
        self.income = income
        self.income_criteria = income_criteria

    def is_valid(self) -> ValidationMessage:
        """ override method to perform income validation """
        status = True
        code = PolicyCodes.ACCEPT

        if self.income < self.income_criteria:
            status = False
            code = PolicyCodes.LOW_INCOME

        return ValidationMessage( status, code.name )
