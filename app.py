from flask import Flask
from flask_restful import Api
from transport_resource import TransportResource

app = Flask(__name__)
api = Api(app)

# Register the TransportResource endpoint
api.add_resource(TransportResource, '/transport')