class Vehicle:
    vehicle_count = 0  # Class variable to count vehicles

    def __init__(self, brand, model, year):
        """Initialize vehicle details and increment counter"""
        self.brand = brand
        self.model = model
        self.year = year
        Vehicle.vehicle_count += 1  # Increase count on new object creation

    @classmethod
    def total_vehicles(cls):
        """Return the total number of vehicles"""
        return cls.vehicle_count

    @staticmethod
    def is_valid_model_year(year):
        """Check if model year is after 2000"""
        return year > 2000

    def display_info(self):
        """Display vehicle details"""
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

#   Create vehicles
car1 = Vehicle("Toyota", "Corolla", 2005)
car2 = Vehicle("Ford", "Mustang", 2018)
car3 = Vehicle("Honda", "Civic", 1999)

#   Check if "1999" is a valid model year
print(f"Is 1999 a valid model year? {Vehicle.is_valid_model_year(1999)}")

#   Display total vehicle count
print(f"Total number of vehicles: {Vehicle.total_vehicles()}")
