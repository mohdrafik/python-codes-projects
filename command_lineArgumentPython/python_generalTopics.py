# sent = "I work for {0} and salary {}"
# comp = "CERN"
# sal = 1000
# print(sent.format(sal,comp))  # evaluate to:  I work for 1000 and salary CERN
# print(sent.format(comp,sal))  # I work for CERN and salary 1000
#
# sent = "I work for {1} and salary {0}"
# comp = "CERN"
# sal = 1000
# print(sent.format(sal,comp))  # evaluate to:  I work for CERN and salary 1000
# # first argument of the tuple(format) is 0 , 1 and so on....
# print(sent.format(comp,sal))  # I work for 1000 and salary CERN
#
# # **** fstring..
# # can directly put variable name in the string directly.
# print(f"I work in {comp} and earn {sal} ")  # I work in CERN and earn 1000
# val = 65.2302356
# x = f"my phone value is {val:.2f} " # this will limit the val variable to 2 decimal digits.
# print(x)  # my phone value is 65.23
#
# print(" this is for the retaining the curly bracket put double curly brackets.")
# print(f" i am in {{ italy }} and continue work in {{CERN}}") # i am in { italy } and continue work in {CERN}
#
# def add(a,b):
#     ''' it will add two value.'''
#     return a+b
#
# print("addition of 2 values =",add(3,4))
# print(add.__doc__)

""" python enhancement proposal (PEP 8)  
   this is to make code readable, maintable.
   go to terminal and type python3 --> enter --> 
   type --> import this --> you will get zen of python : The Zen of Python, by Tim Peters
"""
# arg and kwarg in python.
"""
4 types of arguments, we can give to the function.
1. default arguments. # def  add(a =1,b=3)
2. keyword arguments . # in the function argument directly give the argument by name and value in any order. 
 hence the order in which argument is passed does not matter.   
3. variable length arguments.
4. Required arguments
 

"""


# def average(a=2, b=1):
#     print("the avg: ", (a + b) / 2)
#
#
# average(b=10)  # evaluate to -->  the avg:  6.0
#

# def print_name(fname, mname=" ramu", lname="kaka"):
#     print(f"{fname} {mname} {lname}")
#
# print_name("ajju")

# keyword arguments
# def print_add(a, b):
#     print("val of a = ", a)
#     print("val of b = ", b)
#
#
# print_add(b=200, a=100)


# 3. variable length arguments.
# def avg(*nums):  # this will take arguments as tuple of variable length.
#     print(type(nums))
#     sum = 0
#     for i in nums:
#         sum = sum + i
#     print("Average = ", sum / len(nums))
#
#
# avg(1, 2, 3, 4) # can vary the length of tuple and elements same function will work.

# def print_fullName(**name):
#     print(type(name))
#     print("Hi:",name["fname"],name["mname"],name["lname"])
#
# print_fullName(lname = "singh",mname ="kumar",fname ="Raj")
#

# args and qargs:

def print_args(normal, *args, **kwargs):
    # print()
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(f"{key} and their value:{value}")
        # print(key,value)


kw = {"staish": 'classmate', "mahesh": "farmer", "prem": "engg", "20": "per hour"}
argmnt = ["satish", "mahesh", "prem", 20, 45]
regular = "hi this is regular argument and list is here:"
print_args(regular, argmnt, kw)
