import json
import random

def generate_ticket_id():
    return str(random.randint(100000, 999999))

def book_transport():
    print("Book Transport")
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    age = int(input("Enter your age: "))

    if age < 18:
        permission = input("Do you have parent permission? (yes/no): ")
        if permission.lower() != "yes":
            print("Booking process cancelled. Parent permission required for underage passengers.")
            return

    gender = input("Enter your gender (male/female): ")
    while gender.lower() not in ["male", "female"]:
        print("Invalid gender. Please enter either 'male' or 'female'.")
        gender = input("Enter your gender (male/female): ")

    with open("transport_data.json", "r") as file:
        transport_data = json.load(file)

    print("Transport List:")
    for transport in transport_data:
        print(f"\nTransport ID: {transport['ID']}")
        print(f"Capacity: {transport['CAPACITY']}")
        print(f"Location: {transport['LOCATION']}")
        print(f"Price: {transport['PRICE']}")
        print(f"Description: {transport['DESCRIPTION']}")

    transport_id = int(input("Enter the ID of the transport to book: "))
    found_transport = None
    for transport in transport_data:
        if transport["ID"] == transport_id:
            found_transport = transport
            break

    if found_transport is None:
        print("Invalid transport ID. Booking process cancelled.")
        return

    ticket_summary = {
        "ID": generate_ticket_id(),
        "Name": name,
        "Surname": surname,
        "Age": age,
        "Gender": gender,
        "Transport ID": found_transport["ID"],
        "Transport Capacity": found_transport["CAPACITY"],
        "Transport Location": found_transport["LOCATION"],
        "Transport Price": found_transport["PRICE"],
        "Transport Description": found_transport["DESCRIPTION"]
    }

    with open("ticket_summary.json", "r+") as file:
        data = json.load(file)
        data.append(ticket_summary)
        file.seek(0)
        json.dump(data, file, indent=4)

    print(f"-------------------------------")
    print("\nTicket Summary:")
    print(f"-------------------------------")
    print(f"Ticket ID: {ticket_summary['ID']}")
    print(f"Name: {name}")
    print(f"Surname: {surname}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print(f"-------------------------------")
    print(f"Transport ID: {found_transport['ID']}")
    print(f"Transport Capacity: {found_transport['CAPACITY']}")
    print(f"Transport Location: {found_transport['LOCATION']}")
    print(f"Transport Price: {found_transport['PRICE']}")
    print(f"Transport Description: {found_transport['DESCRIPTION']}")
    print(f"-------------------------------")

    print("\nBooking Successful!")