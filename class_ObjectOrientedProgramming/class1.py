# class person:
#     name = "jamuna"
#     occupation = "Engg"
#     salary = 100
#
#     def print_info(self):
#         """self ka matlab vo object jsike pe ye method call kiya ja rha hai.
#         when this method is called by some object. it will replace self by that object.
#         """
#         print(self.name, " is a", self.occupation, "and earn a amount", self.salary)
#         # print(f"{self.name} ")
#
#
# a = person()
# a.print_info()
# a.name = "ramu"
# a.salary =500
# a.print_info()
# b = person()
# b.name = "mahira"
# b.occupation = "studenti"
# b.salary = "no salary"
# b.print_info()

# constructor -----------------
# class student:
#     def __init__(self,name,occ):
#         """ this is constructor whenever I create object this is called by the default."""
#         self.name = name
#         self.occ = occ
#     def info(self):
#         print(f"hey mY name {self.name} and occupation {self.occ} ")
#
# a = student('ravi','student1') #self is automatically passed  as a.
# b = student('kavita','nurse')  #self is automatically passed  as a.
# a.info()
# b.info()

# ****** Python decorator *********
"""
let's say we want to do arrangement that every function give a message good morning at the starting
and at the end print the thanks for using this function.
- there are two ways by which you can do it - 1. write print function at each function. suppose we have 200 function then
it very tedious to write again again.
2.). write  decorator use it.
"""

# def greet(f1):
#     def f2():
#         print(" welcome !")
#         f1()
#         print("thanks using this function.")
#     return f2
#
#
# @greet    # write decorator before the function. in this way: internally perform this function": greet(hello)()
# def hello():
#     print("!hello worlds :")
#
# # or write: greet(hello)()
# hello()
# #
# def greet(f1):
#     # def f2():
#     print(" welcome !")
#     f1()
#     print("thanks using this function.")
#
#
# # return f2
# @greet  # write decorator before the function. in this way: internally perform this function": greet(hello)()
# def hello():
#     print("!hello worlds :")
# or write: greet(hello)
# hello()


# def greet(f1):
#     def f2(*args, **kwargs):
#         print("!! welcome")
#         f1(*args, **kwargs)
#         print("Thanks !")
#
#     return f2
#
#
# @greet
# def add(*nums):
#     print(sum(nums))
# # or  we can write in this way also.
# # greet(add)(10, 20, 1, 2)
# add(1,6,7,8)


# ********* inheritance:
# class employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     def showDetails(self):
#         print(f"The name of employee: {self.name} an id is {self.id}")
#
#
# class manager(employee):
#     """ manager is a class which is inherited from the employee class.
#       manager --> child class
#       employee --> father class
#     """
#     def showManager(self):
#         print(f" I am manager class method:Attribute --> members and methods of a class is called Attributes ")
#
#
# e1 = employee("raju", 101)
# e1.showDetails()
# # e1.showManager()  #ERROR:  AttributeError: 'employee' object has no attribute 'showManager'
# e2 = manager("kaju", 501)  # e2 is object of the manager class.
# e2.showDetails()
# e2.showManager()

"""
Types of inheritance:
1. single inheritance
2. Multiple inheritance
3. multilevel inheritance
4. hybrid inheritance
"""
# *********** access modifier.
"""
1.public access modifier
2.protected access modifier
3.private access modifier
"""


# In  C++ -->  by default Attributes in C++ are private (access modifier).
# PYTHON -->  by default Attributes in python are PUBLIC (access modifier).

# EXAMPLE:
# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#
#
# a = student("kaju",20)
# print(a.name) # here name is accessed
#
# private access modifier
# there is no strict concept in the python for private access modifier like other programming language
# although A convention exists -> just add double underscore (__name) before the member of the class.
# now name is private attribute(aka member)
# class student:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age
#
#
# a = student("kaju", 20)
# # print(a.__name)  # show error because it is private. but still we can access see below example..
#
#
# class student:
#     def __init__(self, name, age):
#         self.__name = name  # __name for name attribute, for  making private
#         self.age = age
#
#     def __fun(self):
#         print(f"I am of {self.age} and my name {self.__name}")
#         return  "it is private function by convention"
#
#
# a = student("kaju", 20)
# # print(a.__name) # can't not be accessed directly.
# print(a._student__name)  # can be accessed using the class name with underscore (_student__name) and attribute with double underscore
# print(a._student__fun())
# it is done by Name mangling.
# print(a.__dir__())
# NOTE: There is no concept of private, public and protected in python.
# if these (private, public and protected) are used, these are just convention.

# if __(double under score) is there than python do Name mangling. otherwise its' normally behave like public.
# single underscore(_) is just a naming convention,and does not actually provide any protection or restrict access to the member.
# varaible name with _ e.g. _varName. is for making a variable protected.
#
# class employee:
#     def __init__(self, age, name):
#         self._name = name
#         self.age = age
#
#     def _fun1(self):
#         return "this is fun1()"
#
#
# class engg(employee):  # inherited
#     print(" i am inherited.")
#
#
# a = employee(56, "janak")
# b = engg(20 , "kana")
# print(a._name)
# print(a._fun1())
#
# print(b._name)
# print(b._fun1())



































