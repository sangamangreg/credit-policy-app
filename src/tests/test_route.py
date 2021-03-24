""" test routes by creating a client connection """
import unittest
from app import app


class TestPolicy(unittest.TestCase):
    """
    A class to test policy request
    """

    def setUp(self):
        self.client = app.test_client()

    def test_empty_request(self):
        """ Sample test case to setup project """

        res = self.client.post( '/policy-request', json={} )
        json_data = res.get_json()
        self.assertEqual( "REJECT", json_data['status'] )
        self.assertEqual( "LOW_INCOME", json_data['reason_of_rejection'] )

    def test_valid_request(self):
        """ valid scenario """

        res = self.client.post( '/policy-request', json={
            "customer_income": 1000,
            "customer_debt": 500,
            "payment_remarks_12m": 0,
            "payment_remarks": 1,
            "customer_age": 18
        } )
        json_data = res.get_json()
        self.assertEqual( "ACCEPT", json_data['status'] )

    def test_invalid_request_age(self):
        """ Age is invalid """

        res = self.client.post( '/policy-request', json={
            "customer_income": 1000,
            "customer_debt": 500,
            "payment_remarks_12m": 0,
            "payment_remarks": 1,
            "customer_age": 17.99
        } )
        json_data = res.get_json()
        self.assertEqual( "REJECT", json_data['status'] )
        self.assertEqual( "UNDERAGE", json_data['reason_of_rejection'] )

    def test_invalid_request_age_remarks(self):
        """ Age and payment remarks invalid """

        res = self.client.post( '/policy-request', json={
            "customer_income": 1000,
            "customer_debt": 500,
            "payment_remarks_12m": 0,
            "payment_remarks": 2,
            "customer_age": 17.99
        } )
        json_data = res.get_json()
        self.assertEqual( "REJECT", json_data['status'] )
        self.assertEqual( "PAYMENT_REMARKS", json_data['reason_of_rejection'] )

    def test_invalid_request_age_remarks_12m(self):
        """ Age, payment remarks and 12m invalid """

        res = self.client.post( '/policy-request', json={
            "customer_income": 1000,
            "customer_debt": 500,
            "payment_remarks_12m": 1,
            "payment_remarks": 2,
            "customer_age": 17.99
        } )
        json_data = res.get_json()
        self.assertEqual( "REJECT", json_data['status'] )
        self.assertEqual( "PAYMENT_REMARKS", json_data['reason_of_rejection'] )

    def test_invalid_request_age_remarks_12m_debt(self):
        """ Age, payment remarks, 12m, debts invalid """

        res = self.client.post( '/policy-request', json={
            "customer_income": 1000,
            "customer_debt": 501,
            "payment_remarks_12m": 1,
            "payment_remarks": 2,
            "customer_age": 17.99
        } )
        json_data = res.get_json()
        self.assertEqual( "REJECT", json_data['status'] )
        self.assertEqual( "HIGH_DEBT_FOR_INCOME", json_data['reason_of_rejection'] )

    def test_invalid_request_age_remarks_12m_debt_income(self):
        """ Age, payment remarks, 12m, debts and income invalid """

        res = self.client.post( '/policy-request', json={
            "customer_income": 499,
            "customer_debt": 501,
            "payment_remarks_12m": 1,
            "payment_remarks": 2,
            "customer_age": 17.99
        } )
        json_data = res.get_json()
        self.assertEqual( "REJECT", json_data['status'] )
        self.assertEqual( "LOW_INCOME", json_data['reason_of_rejection'] )
