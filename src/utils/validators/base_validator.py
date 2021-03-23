""" File to hold base classes for validators """

from abc import abstractmethod


class ValidationMessage:
    """ A class to hold validation message """
    def __init__(self, status: bool, error_code: str):
        self.status = status
        self.error_code = error_code


class BaseValidator:
    """ A base validator class """

    @abstractmethod
    def is_valid(self) -> ValidationMessage:
        """ an abstract method to validate condition """
        raise NotImplementedError()

    def plus_(self, other: "BaseValidator") -> "AddOnValidator":
        """ method to add two conditions together """
        return AddOnValidator( self, other )


class AddOnValidator( BaseValidator ):
    """ a class to to perform AND operation on two validators in order """

    def __init__(self, validator1: BaseValidator, validator2: BaseValidator):
        self.validator1 = validator1
        self.validator2 = validator2

    def is_valid(self) -> ValidationMessage:
        """ perform and operation on two validators """
        validation1 = self.validator1.is_valid()
        if not validation1.status:
            return validation1

        return self.validator2.is_valid()
