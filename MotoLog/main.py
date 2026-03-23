from data_manager import add_bike  # Imports function in data manager file to save bikes into CSV file

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

def add_bike(registrations, brands, models, mileages): # This function allows usder to add bikes to MotoLog
    print("--- ADD MOTORBIKE ---")

    registration = input("Registration: ").strip().upper()
    brand = input("Brand: ").strip().capitalize()
    model = input("Model: ").strip()
    mileage = input("Mileage: ").strip()

    registrations.append(registration)
    brands.append(brand)
    models.append(model)
    mileages.append(mileage)

    print("Motorbike added successfully.")

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
            print("Search bike by registration selected")
        elif choice == "4":
            print("View all bikes selected")
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