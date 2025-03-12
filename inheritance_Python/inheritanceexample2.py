# super(). to extend the extra functionality of the child.
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def display_info(self):
        print(f" vehicle model: {self.model} \n vehicle brand:{self.brand}")

class Car(Vehicle):
    def __init__(self,brand,model,fueltype):
        super().__init__(brand,model)  # called to the parent constructor
        self.fueltype = fueltype

    def display_info(self):
        super().display_info()
        print(f" fuel type of the vehicle:{self.fueltype}")


car1 = Car("honda","civic","petrol")
car1.display_info()
