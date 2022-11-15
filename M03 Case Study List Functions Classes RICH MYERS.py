class Vehicle
    def __init__(self, car, truck, plane, boat, broomStick):
        self.car = car
        self.truck = truck
        self.plane = plane
        self.boat = boat
        self.broomstick = broomStick

class car(Vehicle)
    def __init__(self, vehicleType, year, make, model, numberOfDoors, roofType):
        print(f"Vehicle type is {self.vehicleType} || Year is {self.year} || Make is {self.make} || Model is {self.model} ||
        Number of doors are {self.numberOfDoors} || Type of roof is {roofType}")    
        self.vehicleType = vehicleType
        self.year = year
        self.make = make
        self.model = model
        self.numberOfDoors = numberOfDoors
        self.roofType = roofType

vehicleType = input("Enter your vehicle type : ")
year = input("Enter the year : ")
make = input("Enter the make of your vehicle : ")
model = input("Enter the model of your vehicle : ")
numberOfDoors = input("Enter the number of doors. ex. 2 door or 4 door : ")
roofType = input("Is your car solid roof or convertible? : ")
