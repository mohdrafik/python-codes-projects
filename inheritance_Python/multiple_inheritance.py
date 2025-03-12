#multiple inheritance
class Father:
    def father_traits(self):
        print("Father is strong.")

class Mother:
    def mother_traits(self):
        print("Mother is caring.")

class Child(Father, Mother):  # Multiple inheritance
    def child_traits(self):
        print("Child inherits both traits.")

c = Child()
c.father_traits()
c.mother_traits()
c.child_traits()
