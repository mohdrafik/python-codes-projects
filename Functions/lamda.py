# lambda [parameters]: expression inline function.
# def double(x):
#     return x*x

# double = lambda x: x ** 2
# print(double(12))

# ********** when use lambda function inside the another function.
#
# def func1(x):
#     """
#      will return lambda function.
#      then you need to invoke the lambda function with arguments.
#      myadd(argument) / e.g. -  myadd(2)
#     """
#     return lambda a: a + x
#
#
# # myadd = func1(10)
#
# print(func1(100)(10))  # result = 22

# ********* pass many arguments in the lambda function:
# avg = lambda x,y,z:(x+y+z)/3
# print(avg(10,2,3))

# ***** passing the lambda function as a argument of the another function.
# def func2(fx, a):
#     return 10 + fx(a)
#
#
# print(func2(lambda x: x ** 2, 10))   # result = 110

# lt1 = [2, 3, 4, 1]
#
# ******** map function *********
# def cube(l):
#     return l ** 3
#
#
# # print(cube(3))
#
# # newl =[]
# newl = list(map(cube, lt1))
#
# print(newl)
# ********* filter function ***********

# lt1 = [2, 3, 4, 10, 12, 21]
#
#
# def filter_fun(x):
#     """
# it will return true if x >2 otherwise False
#     """
#     return x > 2
#
#
# newl = list(filter(filter_fun, lt1))
# print(newl)

# from functools import reduce
#
# lt = [1, 2, 3, 4, 5, 60]
# 
#
# # find the sum of numbers in the list using reduce function.
# def mysum(x, y):
#     return x + y
#
#
# newsum = reduce(mysum, lt)
# print(newsum)
