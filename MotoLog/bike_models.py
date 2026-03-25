class Vehicle: # Parent class for general vehicle details

    def __init__(self, registration, brand, model): # Stores basic vehicle information
        self.registration = registration
        self.brand = brand
        self.model = model


class Motorbike(Vehicle): # Child class that inherits from Vehicle class

    def __init__(self, registration, brand, model, mileage): # Calls the parent class constructor first
        super().__init__(registration, brand, model)

        self.mileage = mileage # Stores the motorbike specific information

    def display_bike(self): # Returns bike details in a readable format
        return f"{self.registration} | {self.brand} | {self.model} | {self.mileage}"