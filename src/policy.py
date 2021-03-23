""" Policy route handle file """
from flask import request
from flask_restful import Resource

from utils.validators.base_validator import ValidationMessage
from utils.validators.policy_validator import CustomerPolicyValidator

from utils.policy_request import PolicyRequest


class Policy( Resource ):
    """ A class to handle request for policy """

    def post(self):
        """ New policy request will come here """

        payload: dict
        payload = request.json  # Content-Type: application/json in req headers

        # creating request object with default values
        policy_request = PolicyRequest(age=payload.get('customer_age', 0),
                                       income=payload.get('customer_income', 0),
                                       debt=payload.get( 'customer_debt', 0 ),
                                       remarks=payload.get( 'payment_remarks', 2 ),
                                       remarks_12m=payload.get('payment_remarks_12m',2))

        validator = CustomerPolicyValidator(policy_request)

        validate_response: ValidationMessage
        validate_response = validator.is_valid()

        res = {'status': "ACCEPT"}

        if not validate_response.status:
            res['status'] = "REJECT"
            res['reason_of_rejection'] = validate_response.error_code

        return res
