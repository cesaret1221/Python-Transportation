# Python-Transportation
Python Transportation Planner System

Transport Booking Console Documentation
The Transport Booking Console is a command-line application that allows users to perform various
actions related to booking and managing transport. It provides a menu-based interface for easy
interaction and includes features such as adding transport data, booking transport, canceling
transport, editing transport details, checking transport availability, and viewing the list of all available
transports.
Prerequisites
Python 3.x installed on the system.
Required modules: json.
Installation
Clone or download the source code from the repository.
Ensure that the required modules are installed by running the following command:
pip install json
Usage
Open a terminal or command prompt.
Navigate to the directory where the source code is located.
Run the following command to start the Transport Booking Console:
python main.py
The console will display a menu with various options. Enter the corresponding number for the action
you want to perform.
Menu Options
Add Transport Data
This option allows you to add transport data to the system. You will be prompted to enter details such
as transport ID, description, capacity, location, and price.
Book Transport
Use this option to book a transport. You will be asked to provide your name, surname, age, gender,
and the ID of the transport you want to book. If you are under 18 years old, parent permission will be
required.
Cancel Transport
With this option, you can cancel a previously booked transport by providing the 6-digit ticket
summary ID. You will be shown the details of the ticket before confirming the cancellation.
Edit Transport
This option allows you to edit the details of a booked transport. You need to provide the 6-digit ticket
summary ID and then enter the updated information, including your name, surname, age, and gender.
Check Transport Availability
Use this option to check the availability of a specific transport. You will be prompted to enter the ID of
the transport, and the system will display the details of the transport along with the number of tickets
sold and the places left.
View All Transport List
Selecting this option will display the complete list of available transports. Each transport will be
shown with its ID, capacity, location, price, description, tickets sold, and places left.
Exit
Choosing this option will terminate the Transport Booking Console.
Data Files
The application uses two JSON files to store data:
transport_data.json: Contains the transport data, including ID, description, capacity, location, and
price.
ticket_summary.json: Stores the ticket summaries, including the ticket ID, passenger details, and
transport details.
Important Notes
Make sure to properly input the required information to ensure accurate booking and cancellation.
The ticket summary ID is a 6-digit alphanumeric code unique to each ticket. Ensure to provide the
correct ID when performing actions related to a booked transport.
License
The Transport Booking Console is released under the MIT License
