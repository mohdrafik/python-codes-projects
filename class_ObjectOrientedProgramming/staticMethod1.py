class Car:
    wheels = 4  # Class variable

    def __init__(self, brand, speed):
        self.brand = brand  # Instance variable
        self.speed = speed  # Instance variable

    def show_info(self):  # Instance method (requires self)
        print(f"Car brand: {self.brand}, Speed: {self.speed}, Wheels: {Car.wheels}")

    @staticmethod
    def general_info():  # Static method (no self, no cls)
        print("Cars generally have an engine and wheels.")

# Creating instance of Car
car1 = Car("Toyota", 120)

# Instance Method (Needs an Object)
car1.show_info()  # Accesses instance and class variables

# Static Method (No Need for Object)
Car.general_info()  # Works without accessing instance or class variables
