""" file to have class with debts validation """
from abc import ABC

from utils.constants import PolicyCodes
from utils.validators.base_validator import BaseValidator, ValidationMessage


class DebtValidator( BaseValidator, ABC ):
    """ class to validate customer debts """
    def __init__(self, debt: float, income: float, debt_criteria: float):
        self.debt = debt
        self.income = income
        self.debt_criteria = debt_criteria

    def is_valid(self) -> ValidationMessage:
        """ override method to perform debts validation """
        status = True
        code = PolicyCodes.ACCEPT

        if ((self.debt / self.income) * 100) > self.debt_criteria:
            status = False
            code = PolicyCodes.HIGH_DEBT_FOR_INCOME

        return ValidationMessage( status, code.name )
