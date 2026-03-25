import csv  # Imports the CSV library so we can work with CSV files
import statistics

def add_bike(registration, brand, model, mileage): # This function allows user to save a bike into bikelog.csv
    with open("MotoLog/bikelog.csv", "a", newline="") as file: # Opens bikelog.csv file, a (append mode) allows it to be added, without deleting old data, and newline prevents blank lines from appearing.
        writer = csv.writer(file) # This create a writer object that lets us write rows into the bikelog.csv file
        writer.writerow([registration, brand, model, mileage]) # Inserts row, and each value goes into a column in the file

def view_all_bikes(): # This function gathers all bikes in the CSV file
    bikes = []  # Empty list to store from the file

    with open("MotoLog/bikelog.csv", "r") as file: # Opens the csv file in r (read mode)
        reader = csv.reader(file)  # reader lets us go through each row in the file

        for row in reader:  # Loops through every row in the csv file
            bikes.append(row)  # Adds each row into the list

    return bikes

def update_mileage(registration, new_mileage): # This function updates the mileage of a bike.
    bikes = []  # List will store all the rows from the CSV file
    found = False 

    with open("MotoLog/bikelog.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader: # Checks if this row matches the registration number
            if row[0] == registration:
                row[3] = new_mileage  # Changes the mileage column
                found = True 

            bikes.append(row)

    with open("MotoLog/bikelog.csv", "w", newline="") as file: 
        writer = csv.writer(file)

        for row in bikes: # Writes every row back into the CSV file
            writer.writerow(row)

    return found

def delete_bike(registration): # This function removes a bike from the csv file
    bikes = [] 
    found = False 

    with open("MotoLog/bikelog.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader: # Skips the bike the user wants to delete
            if row[0] == registration:
                found = True
                continue 

            bikes.append(row)  # Keeps all other rows

    with open("MotoLog/bikelog.csv", "w", newline="") as file: # Rewrite the file with remaining bikes
        writer = csv.writer(file)

        for row in bikes:
            writer.writerow(row)

    return found

def add_service_record(registration, date, service, cost): # This function allows users to save a service record into the new services CSV file
    with open("MotoLog/services.csv", "a", newline="") as file: # a = add new row
        writer = csv.writer(file)
        writer.writerow([registration, date, service, cost]) # One service record = one row

def view_service_analytics(): # This function calculates the total of services and average cost
    costs = []  # List to store all service costs
    count = 0 

    with open("MotoLog/services.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == "registration":
                continue  

            count += 1  # Increase total service count

            try:
                cost = float(row[3])  # Convert cost to a number
                costs.append(cost)
            except:
                pass 

    if count == 0: # No services
        return 0, 0  

    average = statistics.mean(costs)  # This calculates the average

    return count, average