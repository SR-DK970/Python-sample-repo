class Vehicle:

    # This function will construct an object with parameters that we provide, when we actually created object.
    # Define a function with parameters
    # Class definition was created, but we are not doing anything with it.
    def __init__(self, vehicle_name, distance_in_km, time_in_hours, fuel_in_ltrs):
        self.name_of_vehicle = vehicle_name
        self.distance_travelled = distance_in_km
        self.time_taken = time_in_hours
        self. amount_of_fuel_consumed = fuel_in_ltrs

    # Create a function to measure speed of vehicle and pass self as parameter to access class attributes
    def find_max_speed_of_vehicle(self):
        max_speed_of_vehicle = self.distance_travelled / self.time_taken
        print(f"Maximum speed of the Vehicle {self.name_of_vehicle} is {max_speed_of_vehicle} kilometers per hour.")
        return max_speed_of_vehicle

    def find_mileage_of_vehicle(self):
        mileage_of_vehicle = self.distance_travelled / self.amount_of_fuel_consumed
        print(f"Mileage of the {self.name_of_vehicle} is {mileage_of_vehicle} kilometers per one liter.")
        return mileage_of_vehicle


    # Function to get vehicle information
    def vehicle_info(self):
        print(f"Vehicle type is {self.name_of_vehicle}.")




