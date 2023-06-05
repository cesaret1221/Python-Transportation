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

def edit_transport():
    print("Edit Transport")
    ticket_id = input("Enter the 6-digit ticket summary ID: ")

    ticket_data = load_ticket_data()
    found_ticket = None
    for ticket in ticket_data:
        if ticket["ID"] == ticket_id:
            found_ticket = ticket
            break

    if found_ticket is None:
        print("Invalid ticket ID. Editing process cancelled.")
        return

    print("Existing Ticket Summary:")
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

    print("\nProvide updated information:")
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    age = int(input("Enter your age: "))

    if age < 18:
        permission = input("Do you have parent permission? (yes/no): ")
        if permission.lower() != "yes":
            print("Editing process cancelled. Parent permission required for underage passengers.")
            return

    gender = input("Enter your gender (male/female): ")
    while gender.lower() not in ["male", "female"]:
        print("Invalid gender. Please enter either 'male' or 'female'.")
        gender = input("Enter your gender (male/female): ")

    found_ticket["Name"] = name
    found_ticket["Surname"] = surname
    found_ticket["Age"] = age
    found_ticket["Gender"] = gender

    save_ticket_data(ticket_data)

    print(f"-------------------------------")
    print("\nUpdated Ticket Summary:")
    print(f"-------------------------------")
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
    print(f"-------------------------------")