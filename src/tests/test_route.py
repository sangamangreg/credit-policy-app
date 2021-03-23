import unittest
from app import app


class TestPolicyRequest(unittest.TestCase):
    """
    A class to test policy request
    """

    def test_sample(self):
        """ Sample test case to setup project """
        with app.test_client() as c:
            rv = c.post( '/policy-request', json={
                "age": 2
            } )
            json_data = rv.get_json()
            print(json_data['status'])
