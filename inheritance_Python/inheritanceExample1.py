# class animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def sound(self):
#         return f"sound of animal:generic"
    
# class dog(animal):
#     # Dog is also a Animal, Dog is child class(sub class) and Animal is parent class(super class).
#     def sound(self):
#         return f"woof ! woof!"
    
# class cat(animal):
#     def sound(self):
#         return f" meow! meow! "

# # d1= animal("tommy",5)
# # print(d1.sound())
# d2 = dog("tommy",5)
# print(d2.sound()) # output: woof ! woof!
# d3 = cat("jamini",12) 
# print(d3.sound())   #  meow! meow! 

# multiple inheritance:
class Father:
    def father_method(self):
        return " I am father method"

class Mother:
    def mother_method(self):
        return " I am Mother method"

class child(Father,Mother):  # inherit from both mother and father.
    def child_method(self):
        return f" I am child inherited from both method"
        


c1 = child()
# print(c1.father_method())
# print(c1.mother_method())
print(c1.child_method())


















