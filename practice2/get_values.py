
from vehicle_info import Vehicle

# Create an object use name of the class to create an object from main class(in bg it calls init func)
vehicle_info_one = Vehicle("Bus", 92, 2.40, 4)     # Create new object and assign values into a variable
#vehicle_info_one.vehicle_info()
vehicle_info_one.find_max_speed_of_vehicle()
vehicle_info_one.find_mileage_of_vehicle()
