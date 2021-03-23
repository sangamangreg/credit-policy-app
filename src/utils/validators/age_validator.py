""" file to have class with age validation """
from abc import ABC

from utils.constants import PolicyCodes
from utils.validators.base_validator import BaseValidator, ValidationMessage


class AgeValidator( BaseValidator, ABC ):
    """ class to validate customer age """
    def __init__(self, age: float, age_criteria: float):
        self.age = age
        self.age_criteria = age_criteria

    def is_valid(self) -> ValidationMessage:
        """ override method to perform age validation """
        status = True
        code = PolicyCodes.ACCEPT

        if self.age < self.age_criteria:  # age in years. eg. 18.2 years
            status = False
            code = PolicyCodes.UNDERAGE

        return ValidationMessage( status, code.name )
