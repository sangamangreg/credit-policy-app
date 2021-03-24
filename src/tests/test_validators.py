""" A unit test case file for all validators """
import unittest

from utils.validators.age_validator import AgeValidator
from utils.validators.income_validator import IncomeValidator
from utils.validators.debt_validator import DebtValidator
from utils.validators.remarks_validator import PaymentRemarksValidator

from utils.validators.base_validator import ValidationMessage
from utils.constants import PolicyCodes

from utils.validators.remarks_validator import PaymentRemarks12MValidator


class TestValidators(unittest.TestCase):
    """ Perform all unit test case operations """

    def test_age_validator_valid_case(self):
        """ test valid age validator """
        validator = AgeValidator(age=18, age_criteria=18)
        validation : ValidationMessage
        validation = validator.is_valid()
        self.assertTrue(validation.status)

    def test_age_validator_invalid_case(self):
        """ test edge case for age validator """
        validator = AgeValidator(age=17.99, age_criteria=18)
        validation : ValidationMessage
        validation = validator.is_valid()
        self.assertFalse(validation.status)
        self.assertEqual(PolicyCodes.UNDERAGE.name, validation.error_code)

    def test_age_validator_changing_criteria(self):
        """ test age validator with different criteria """
        validator = AgeValidator(age=17.99, age_criteria=17.99)
        validation : ValidationMessage
        validation = validator.is_valid()
        self.assertTrue(validation.status)

    def test_income_validator_valid_case(self):
        """ test valid income validator """
        validator = IncomeValidator(income=500, income_criteria=500)
        validation : ValidationMessage
        validation = validator.is_valid()
        self.assertTrue(validation.status)

    def test_income_validator_invalid_case(self):
        """ test edge case for income validator """
        validator = IncomeValidator( income=499.99, income_criteria=500 )
        validation : ValidationMessage
        validation = validator.is_valid()
        self.assertFalse(validation.status)
        self.assertEqual(PolicyCodes.LOW_INCOME.name, validation.error_code)

    def test_income_validator_changing_criteria(self):
        """ test income validator with different criteria """
        validator = IncomeValidator( income=499.99, income_criteria=499.99 )
        validation : ValidationMessage
        validation = validator.is_valid()
        self.assertTrue(validation.status)

    def test_debts_validator_valid_case(self):
        """ test valid debts validator """
        validator = DebtValidator(debt=500, income=1000, debt_criteria=50)
        validation : ValidationMessage
        validation = validator.is_valid()
        self.assertTrue(validation.status)

    def test_debts_validator_invalid_case(self):
        """ test edge case for debt validator """
        validator = DebtValidator( debt=501, income=1000, debt_criteria=50 )
        validation : ValidationMessage
        validation = validator.is_valid()
        self.assertFalse(validation.status)
        self.assertEqual( PolicyCodes.HIGH_DEBT_FOR_INCOME.name,
                          validation.error_code )

    def test_debts_validator_changing_criteria(self):
        """ test debt validator with different criteria """
        validator = DebtValidator( debt=510, income=1000, debt_criteria=51 )
        validation : ValidationMessage
        validation = validator.is_valid()
        self.assertTrue(validation.status)

    def test_pay_remarks_validator_valid_case(self):
        """ test valid remarks validator """
        validator = PaymentRemarksValidator(remarks=1, criteria_remarks=1)
        validation : ValidationMessage
        validation = validator.is_valid()
        self.assertTrue(validation.status)

    def test_pay_remarks_validator_invalid_case(self):
        """ test edge case for remarks validator """
        validator = PaymentRemarksValidator( remarks=2, criteria_remarks=1 )
        validation : ValidationMessage
        validation = validator.is_valid()
        self.assertFalse(validation.status)
        self.assertEqual( PolicyCodes.PAYMENT_REMARKS.name,
                          validation.error_code )

    def test_pay_remarks_validator_changing_criteria(self):
        """ test remarks validator with different criteria """
        validator = PaymentRemarksValidator( remarks=2, criteria_remarks=2 )
        validation : ValidationMessage
        validation = validator.is_valid()
        self.assertTrue(validation.status)

    def test_pay_remarks_12m_validator_valid_case(self):
        """ test valid remarks 12m validator """
        validator = PaymentRemarks12MValidator( remarks_12m=0, criteria_12m=0 )
        validation : ValidationMessage
        validation = validator.is_valid()
        self.assertTrue(validation.status)

    def test_pay_remarks_12m_validator_invalid_case(self):
        """ test edge case for remarks 12m validator """
        validator = PaymentRemarks12MValidator( remarks_12m=1, criteria_12m=0 )
        validation : ValidationMessage
        validation = validator.is_valid()
        self.assertFalse(validation.status)
        self.assertEqual( PolicyCodes.PAYMENT_REMARKS_12M.name,
                          validation.error_code )

    def test_pay_remarks_12m_validator_changing_criteria(self):
        """ test remarks 12m validator with different criteria """
        validator = PaymentRemarks12MValidator( remarks_12m=1, criteria_12m=1 )
        validation : ValidationMessage
        validation = validator.is_valid()
        self.assertTrue(validation.status)
