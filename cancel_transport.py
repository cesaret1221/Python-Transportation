import json

def load_ticket_data():
    try:
        with open("ticket_summary.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    
    return data

def save_ticket_data(data):
    with open("ticket_summary.json", "w") as file:
        json.dump(data, file, indent=4)

def cancel_transport():
    print("Cancel Transport")
    ticket_id = input("Enter the 6-digit ticket summary ID: ")

    ticket_data = load_ticket_data()
    found_ticket = None
    for ticket in ticket_data:
        if ticket["ID"] == ticket_id:
            found_ticket = ticket
            break

    if found_ticket is None:
        print("Invalid ticket ID. Cancellation process cancelled.")
        return

    print("Ticket Summary:")
    print(f"Ticket ID: {found_ticket['ID']}")
    print(f"Name: {found_ticket['Name']}")
    print(f"Surname: {found_ticket['Surname']}")
    print(f"Age: {found_ticket['Age']}")
    print(f"Gender: {found_ticket['Gender']}")
    print(f"Transport ID: {found_ticket['Transport ID']}")
    print(f"Transport Capacity: {found_ticket['Transport Capacity']}")
    print(f"Transport Location: {found_ticket['Transport Location']}")
    print(f"Transport Price: {found_ticket['Transport Price']}")
    print(f"Transport Description: {found_ticket['Transport Description']}")

    confirmation = input("Are you sure you want to cancel your ticket? (yes/no): ")
    if confirmation.lower() == "yes":
        ticket_data.remove(found_ticket)
        save_ticket_data(ticket_data)
        print("Ticket cancellation successful.")
    else:
        print("Ticket cancellation process cancelled.")