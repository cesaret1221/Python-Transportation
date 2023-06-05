import json

def load_transport_data():
    try:
        with open("transport_data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    
    return data

def view_all_transport_list():
    print("View All Transport List")
    transport_data = load_transport_data()

    if len(transport_data) == 0:
        print("No transport data available.")
    else:
        print("Transport List:")
        for transport in transport_data:
            transport_id = transport["ID"]
            capacity = transport["CAPACITY"]
            location = transport["LOCATION"]
            price = transport["PRICE"]
            description = transport["DESCRIPTION"]

            print(f"\nTransport ID: {transport_id}")
            print(f"Capacity: {capacity}")
            print(f"Location: {location}")
            print(f"Price: {price}")
            print(f"Description: {description}")

if __name__ == "__main__":
    view_all_transport_list()