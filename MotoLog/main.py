from data_manager import add_bike, view_all_bikes, update_mileage, delete_bike, add_service_record, view_service_analytics  # Imports bike functions from data_manager file
from bike_models import Motorbike
import re  # Regular expressions

def is_valid_registration(reg): # Checks reg plate format. e.g. AB12 CDE
    pattern = r"^[A-Z]{2}[0-9]{2}\s[A-Z]{3}$"
    if re.match(pattern, reg):
        return True
    else:
        return False

def is_valid_date(date): # This function checks if the date is in the DD/MM/YYYY format.
    pattern = r"^\d{2}/\d{2}/\d{4}$"
    if re.match(pattern, date):
        return True
    else:
        return False

def display_menu(user_name):
    print ("-------------------------")
    print("WELCOME TO MOTOLOG")
    print("WELCOME BACK: ", user_name)
    print ("-------------------------")

    print("--- MENU ---") # menu and options available to user to choose from
    print("1/ Add motorbike")
    print("2/ Log service record")
    print("3/ Search bike by registration")
    print("4/ View all bikes")
    print("5/ Update mileage")
    print("6/ Delete bike")
    print("7/ Service analytics")
    print("8/ Exit")

    option = input("Select option: ").strip() # .strip() = removes any accidental spaces
    return option

def main():
    name = input("Enter your name: ") # Asks user for username at the beginning of the program
    print(f"\nWelcome, {name}!")

    while True:
        choice = display_menu(name)

        if choice == "1":
            print("\n--- ADD MOTORBIKE ---")
            registration = input("Enter registration: ").strip().upper()  # .strip() = Removes any spaces, .upper() = makes it uppercase
            brand = input("Enter brand: ").strip()
            model = input("Enter model: ").strip()
            mileage = input("Enter mileage: ").strip()

            if not is_valid_registration(registration):
                print("Invalid registration format. Please adhere to the AB12 CDE format.")
            else:
                new_bike = Motorbike(registration, brand, model, mileage)# Creates a Motorbike object using the class

                add_bike(new_bike.registration, new_bike.brand, new_bike.model, new_bike.mileage) # Saves object data into the CSV file

                print("Motorbike added successfully!")
                print("Bike added:", new_bike.display_bike())
        elif choice == "2":
            print("\n--- LOG SERVICE RECORD ---")
        
            registration = input("Enter registration: ").strip().upper()

            bikes = view_all_bikes()
            found = False

            for i in range(1, len(bikes)): # Checks if the bike exists before asking for service details.
                if bikes[i][0] == registration:
                    print("\nBike found:")
                    print(bikes[i][0], "|", bikes[i][1], "|",bikes[i][2], "|", bikes[i][3])
                    found = True
                    break

            if not found:
                print("No bike found with that registration.")

            else: # Only asks for service info if the bike actually exists on record.
                date = input("Enter service date (DD/MM/YYYY): ").strip()
                service = input("Enter service type: ").strip().title()
                cost = input("Enter the cost of service: ").strip()

                if not is_valid_date(date):
                    print("Invalid date format. Use DD/MM/YYYY")
                else:
                    confirm = input("Are these details correct? (yes/no): ").strip().lower()

                    if confirm == "yes" or confirm == "y":
                        add_service_record(registration, date, service, cost)
                        print("Service record added successfully!")
                    else:
                        print("Service record cancelled.")

        elif choice == "3":
            print("\n--- SEARCH BIKE ---")

            search_reg = input("Enter registration: ").strip().upper() # Prompt asks user for registration for the search

            bikes = view_all_bikes() # Gathers all bikes from the csv file

            found = False  # Flag to track if we found a match

            for i in range(1, len(bikes)):
                if bikes[i][0] == search_reg:  # Compares registration
                    print("Found:", bikes[i][0], "|", bikes[i][1], "|", bikes[i][2], "|", bikes[i][3])
                    found = True
                    break 

            if not found:
                print("No bike found with that registration.")

        elif choice == "4":
            print("\n--- VIEW ALL BIKES ---")

            bikes = view_all_bikes() # Calls function to pull all bikes in CSV file.

            if len(bikes) <= 1: # If CSV file only has the header, or is empty, prints below message.
                print("No bikes found.")

            else:
                for i in range(1, len(bikes)): # List starts from row 1, so that the header row is skipped.
                    print("Registration:", bikes[i][0], "| Brand:", bikes[i][1], "| Model:", bikes[i][2], "| Mileage:", bikes[i][3])
                    
        elif choice == "5":
            print("\n--- UPDATE MILEAGE ---")

            registration = input("Enter registration: ").strip().upper()

            bikes = view_all_bikes()

            found = False  # Check if the bike exists

            for i in range(1, len(bikes)): # Loop through bikes to check if registration exists (Skips the header again)
                if bikes[i][0] == registration:
                    found = True
                    break

            if not found:
                print("No bike found with that registration.")
    
            else:
                new_mileage = input("Enter new mileage: ").strip()

                updated = update_mileage(registration, new_mileage)

                if updated:
                    print("Mileage updated successfully!")

        elif choice == "6":
            print("\n--- DELETE BIKE ---")

            registration = input("Enter registration: ").strip().upper()

            bikes = view_all_bikes()
            found = False

            for i in range(1, len(bikes)): # Find bike details and display for user to confirm
                if bikes[i][0] == registration:
                    print("\nBike found:")
                    print(bikes[i][0], "|", bikes[i][1], "|", bikes[i][2], "|",bikes[i][3])
                    found = True
                    break

            if not found:
                print("No bike found with that registration.")

            else:
                confirm = input("\nProceed with deleting this bike? (Y/N): ").strip().lower()

                if confirm == "Y":
                    deleted = delete_bike(registration)

                    if deleted:
                        print("Bike deleted successfully!")
                else:
                    print("Deletion cancelled.")

        elif choice == "7":
            print("\n--- SERVICE ANALYTICS ---")

            result = view_service_analytics() 

            total = result[0]  # total number of services
            average = result[1]  # average service cost

            if total == 0:
                print("No service records found.")
            else:
                print("Total services:", total)
                print("Average cost: £", round(average, 2))

if __name__ == "__main__":
    main()