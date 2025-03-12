# hierarchical inheritance:
class Parent:
    def parent_method(self):
        print("This is the Parent class.")

class Child1(Parent):
    def child1_method(self):
        print("This is Child1.")

class Child2(Parent):
    def child2_method(self):
        print("This is Child2.")

c1 = Child1()
c2 = Child2()

c1.parent_method()  # Inherited from Parent , This is the Parent class
c1.child1_method() # This is Child1.

c2.parent_method()  # Inherited from Parent, This is the Parent class.
c2.child2_method() # This is Child2.
