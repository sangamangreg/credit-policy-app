""" Application start file """

from flask import Flask
from flask_restful import Api

from policy import Policy

app = Flask(__name__)
api = Api( app )

api.add_resource( Policy, '/policy-request' )


if __name__ == '__main__':
    app.run( debug=True, host='0.0.0.0' )
