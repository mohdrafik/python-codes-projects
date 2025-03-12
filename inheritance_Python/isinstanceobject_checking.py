class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()
print(isinstance(d, Dog))    # True
print(isinstance(d, Animal)) # True (because Dog is a subclass of Animal)
print(isinstance(d, object)) # True (all classes inherit from object)



print(issubclass(Dog, Animal)) # True
print(issubclass(Animal, Dog)) # False
