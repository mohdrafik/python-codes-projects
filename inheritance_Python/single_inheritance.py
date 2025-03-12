class Parent:
    def show(self):
        print("This is the Parent class.")

class Child(Parent):
    def display(self):
        print("This is the Child class.")

c = Child()
c.show()   # Inherited method
c.display()
