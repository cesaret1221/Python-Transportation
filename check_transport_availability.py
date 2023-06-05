import json

def load_transport_data():
    try:
        with open("transport_data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    
    return data

def load_ticket_data():
    try:
        with open("ticket_summary.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    
    return data

def count_tickets(transport_id):
    ticket_data = load_ticket_data()
    count = 0
    for ticket in ticket_data:
        if str(ticket["Transport ID"]) == str(transport_id):
            count += 1
    return count

def check_transport_availability():
    print("Check Transport Availability")
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

            ticket_count = count_tickets(transport_id)
            places_left = capacity - ticket_count

            print(f"\nTransport ID: {transport_id}")
            print(f"Capacity: {capacity}")
            print(f"Location: {location}")
            print(f"Price: {price}")
            print(f"Description: {description}")
            print(f"Tickets Sold: {ticket_count}")
            print(f"Places Left: {places_left}")

    transport_id = input("Enter the ID of the transport to check availability: ")
    found_transport = None
    for transport in transport_data:
        if transport["ID"] == transport_id:
            found_transport = transport
            break

    if found_transport is None:
        print("Invalid transport ID.")
    else:
        ticket_data = load_ticket_data()
        tickets_sold = []
        for ticket in ticket_data:
            if str(ticket["Transport ID"]) == str(transport_id):
                tickets_sold.append(ticket)
        
        ticket_count = len(tickets_sold)
        places_left = found_transport["CAPACITY"] - ticket_count

        print(f"\nTransport ID: {transport_id}")
        print(f"Capacity: {found_transport['CAPACITY']}")
        print(f"Location: {found_transport['LOCATION']}")
        print(f"Price: {found_transport['PRICE']}")
        print(f"Description: {found_transport['DESCRIPTION']}")
        print(f"Tickets Sold: {ticket_count}")
        print(f"Places Left: {places_left}")

        if ticket_count > 0:
            print("\nTickets Sold:")
            for ticket in tickets_sold:
                print(f"Ticket ID: {ticket['ID']}")
                print(f"Name: {ticket['Name']}")
                print(f"Surname: {ticket['Surname']}")
                print(f"Age: {ticket['Age']}")
                print(f"Gender: {ticket['Gender']}")
                print("----------------------")