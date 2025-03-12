# If the child class redefines a method that exists in the parent class, 
# the child class’s method overrides the parent’s version.
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

a = Animal()
d = Dog()
c = Cat()

print(a.speak())  # Output: Some sound
print(d.speak())  # Output: Woof!
print(c.speak())  # Output: Meow!
