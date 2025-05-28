# def is_even(x):
#     """ return true if x is even"""
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
#
# for i in range(10):
#     if is_even(i):
#         print(i, "even")
#     else:
#         print(i, "odd")
#
#
# def checkCharacter(char, str):
#     """" input character check if it is available or not in the string"""
#     if char in str:
#         print(char, "is match in str")
#     else:
#         print(char, "NOT match")
#
# checkCharacter('a', "rafik")
# print(checkCharacter('r', "rafik"))

# def f(y):
#     x = 1
#     x += 1
#     print(x)
#
# x = 5
# f(x)
# print(x)
#
# x = 10
# # g(x)  this is an Error :" NameError: name 'g' is not defined "
# def g(y):
#     print(x)  # local scope
#     print(x + 1)
#
# x = 5  # this x is in global scope.
# g(x)    # earlier before th eg function x is ; 10 but g() return according to the most recent value of x which is x =5
# print(x)
"""
result of this program is :
5
6
5
"""
"""  this is crucial example:
   will give error --> UnboundLocalError: local variable 'x' referenced before assignment
 below the function try to use the global variable x that is define outside the function scope.
 can access the outside variable but can't modified. x+=1 try to modified it.
 want modification( bound to new value to x ) define in the function scope first. like x = 0 then you can modified it. 
"""
# def h(y):
#     x += 1    # error is here.
#
# x = 5
# h(x)
# print(x)
