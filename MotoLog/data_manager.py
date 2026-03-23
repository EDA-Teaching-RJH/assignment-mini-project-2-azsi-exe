import csv  # Imports the CSV library so we can work with CSV files

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