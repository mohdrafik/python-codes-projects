class car:

    """
    Why Can't We Have Two __init__ Methods?
    Python does not support method overloading in the traditional sense (like Java or C++).
    The last defined __init__ method overwrites the previous one.
    Instead, use default values in the constructor or alternative constructors
     using @classmethod.
        @classmethod
        def default_car(cls):
            return cls("Honda", "Accord", 1950, 10)

        def display_info(self):
            print(
                f"Car brand: {self.brand}\nCar model: {self.model}\nYear: {self.year}\nMileage: {self.mileage}\n")

    # Using class method to create default car
    car1 = Car.default_car()
    car1.display_info()
    

"""
   # def __init__(self):
   #     self.brand = "honda"
   #     self.year = 1950
   #     print("default constructor")

    def __init__(self, brand:str, model:str, year:int, mileage:int):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        print("parameterized constructor i am using \n ")


    def display_info(self):
        print(
            f"Car brand is: {self.brand} \n car model :{self.model} \n car year of purchase:{self.year} \n car mileage is :{self.mileage} \n ")


c1 = car("honda", 2012,1960,21)
c1.display_info()
