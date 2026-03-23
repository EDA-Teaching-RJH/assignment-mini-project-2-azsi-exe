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