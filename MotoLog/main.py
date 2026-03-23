from data_manager import add_bike, view_all_bikes  # Imports functions from data manager, and works with CSV file.

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

            add_bike(registration, brand, model, mileage) # Calls add bike function to save bike

            print("Motorbike added sucessfully!")

        elif choice == "2":
            print("Log service record selected")
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
            print("Update mileage selected")
        elif choice == "6":
            print("Delete bike selected")
        elif choice == "7":
            print("Service analytics selected")
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()