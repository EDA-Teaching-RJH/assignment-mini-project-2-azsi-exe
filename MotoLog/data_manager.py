import csv  # Imports the CSV library so we can work with CSV files

def save_bike(registration, brand, model, mileage): # This function allows user to save a bike into bikelog.csv
    with open("bikes.csv", "a", newline="") as file: # Opens bikelog.csv file, a (append mode) allows it to be added, without deleting old data, and newline prevents blank lines from appearing.
        writer = csv.writer(file) # This create a writer object that lets us write rows into the bikelog.csv file
        writer.writerow([registration, brand, model, mileage]) # Inserts row, and each value goes into a column in the file