import json

def add_transport_data():
    print("Add Transport Data")
    transport_id = input("Enter transport ID: ")
    description = input("Enter transport description: ")
    capacity = input("Enter transport capacity: ")
    location = input("Enter transport location: ")
    price = input("Enter transport price: ")

    transport = {
        "ID": int(transport_id),
        "DESCRIPTION": description,
        "CAPACITY": int(capacity),
        "LOCATION": int(location),
        "PRICE": float(price)
    }

    with open("transport_data.json", "r") as file:
        transport_data = json.load(file)

    transport_data.append(transport)

    with open("transport_data.json", "w") as file:
        json.dump(transport_data, file, indent=4)

    print("Transport data added successfully!")