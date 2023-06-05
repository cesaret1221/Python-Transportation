import json

def load_transport_data():
    try:
        with open('transport_data.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_transport_data(transport_data):
    with open('transport_data.txt', 'w') as file:
        json.dump(transport_data, file)

# Load the transport data from the file
transport_data = load_transport_data()