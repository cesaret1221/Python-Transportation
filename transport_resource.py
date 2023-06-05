from flask import request
from flask_restful import Resource
import add_transport_data

class TransportResource(Resource):
    def get(self):
        return add_transport_data.load_transport_data(), 200

    def post(self):
        transport_data = add_transport_data.load_transport_data()
        transport_data = request.get_json()
        add_transport_data.save_transport_data(transport_data)
        return transport_data, 201