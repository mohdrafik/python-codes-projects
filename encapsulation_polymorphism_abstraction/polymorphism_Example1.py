# Parent Class
class Animal:
    def speak(self):
        return "Some generic animal sound"

# Child Class - Dog
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

# Child Class - Cat
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Child Class - Cow
class Cow(Animal):
    def speak(self):
        return "Moo!"

# ✅ Testing Polymorphism
animals = [Dog(), Cat(), Cow()]  # List of different animals

count = 0
for animal in animals:
    # print(f"name of animal: {animal}")
    # inst = f"animal{count+1}"
    # print(inst)
    o11 = animal
    # print(o11)
    print(o11.speak())
    # print(animal.speak())  # Calls respective speak() method
