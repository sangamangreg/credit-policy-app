""" Policy request handle file """
from flask import request
from flask_restful import Resource


class PolicyRequest( Resource ):
    """ A class to handle request for policy """

    def post(self):
        """ New policy request will come here """

        payload = request.json  # Content-Type: application/json in req headers
        return {"status": "ACCEPT"}
