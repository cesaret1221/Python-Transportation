import add_transport_data
import book_transport
import cancel_transport
import edit_transport
import check_transport_availability
import view_all_transport_list

def main():
    print("Transport Booking Console")
    print("-------------------------")
    while True:
        print("\nMenu:")
        print("1. Add Transport Data")
        print("2. Book Transport")
        print("3. Cancel Transport")
        print("4. Edit Transport")
        print("5. Check Transport Availability")
        print("6. View All Transport List")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_transport_data.add_transport_data()
        elif choice == "2":
            book_transport.book_transport()
        elif choice == "3":
            cancel_transport.cancel_transport()
        elif choice == "4":
            edit_transport.edit_transport()
        elif choice == "5":
            check_transport_availability.check_transport_availability()
        elif choice == "6":
            view_all_transport_list.view_all_transport_list()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()