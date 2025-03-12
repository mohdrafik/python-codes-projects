class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def display1(self):
        print(f"name : {self.name}, age :{self.age} ")


class Employee(Person):
    def __init__(self, name, age ,salary):
        super().__init__(name,age)
        self.salary = salary
    def display2(self):
        print(f"name : {self.name}, age :{self.age}, salary :{self.salary}")

class Manager(Employee):
    def __init__(self,name,age,salary,Teamsize):
        super().__init__(name,age,salary)
        self.Teamsize = Teamsize
    def display(self):
        print(f"name : {self.name}, age :{self.age} , salary :{self.salary}, teamsize: {self.Teamsize}")


M1 = Manager('janaki',52,1000,3)
M1.display()
M1.display1()
M1.display2()