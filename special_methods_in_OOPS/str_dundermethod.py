class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

        # pass

    def __str__(self):
            return f"name: {self.name} and age:{self.age}"
        
person = Person("janu",35)
# print(person)   #  output without the __str__(self) method: --> <__main__.Person object at 0x000001B6B96E8BE0>
print(person)   #  output with the __str__(self) method: -->  name: janu and age:35