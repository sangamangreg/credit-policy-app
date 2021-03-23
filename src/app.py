""" Application start file """

from flask import Flask
from flask_restful import Api

from policy_request import PolicyRequest

app = Flask(__name__)
api = Api( app )

api.add_resource( PolicyRequest, '/policy-request' )


if __name__ == '__main__':
    app.run( debug=True, host='0.0.0.0' )
