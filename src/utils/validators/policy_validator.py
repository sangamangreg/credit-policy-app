""" file to hold policy validator """
from abc import ABC

from utils.validators.base_validator import BaseValidator

from utils.constants import PolicyCriteria
from utils.validators.age_validator import AgeValidator
from utils.validators.base_validator import ValidationMessage
from utils.validators.debt_validator import DebtValidator
from utils.validators.income_validator import IncomeValidator
from utils.validators.remarks_validator import PaymentRemarksValidator
from utils.validators.remarks_validator import PaymentRemarks12MValidator

from utils.policy_request import PolicyRequest


class CustomerPolicyValidator( BaseValidator, ABC ):
    """ validate policy request """
    def __init__(self, policy_request: PolicyRequest):
        self.policy_request = policy_request

    def is_valid(self) -> ValidationMessage:
        """ override function to validate policy request based on order """

        income_check = IncomeValidator( income=self.policy_request.income,
                                        income_criteria=PolicyCriteria.INCOME )

        debt_check = DebtValidator( debt=self.policy_request.debt,
                                    income=self.policy_request.income,
                                    debt_criteria=PolicyCriteria.DEBT )

        age_check = AgeValidator( age=self.policy_request.age,
                                  age_criteria=PolicyCriteria.AGE )

        remarks_check = PaymentRemarksValidator(
            remarks=self.policy_request.remarks,
            criteria_remarks=PolicyCriteria.remarks )

        remarks_12m_check = PaymentRemarks12MValidator(
            remarks_12m=self.policy_request.remarks_12m,
            criteria_12m=PolicyCriteria.remarks_12m )

        # maintain order - important step of validation
        validator = income_check.plus_(debt_check.plus_(
            remarks_check.plus_( remarks_12m_check.plus_( age_check ) ) ) )

        # return validation message with ACCEPT | REJECT
        return validator.is_valid()
