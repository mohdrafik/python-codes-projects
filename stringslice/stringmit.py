# s = "rafik"
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print("using the negative index:\n")
# print(s[-1])
# print(s[-2])
# print(s[-3])
# print(s[-4])
# print(s[-5])
# s = "JAKIR"
# count = -1
# for i in s:
#     count += 1
#     print("s [", count, "]", end='')
#     print("  -->  evaluate to ", i)
# print("The Following  is for negative indexing:")
# l = len(s)
# r = 0   # for indexing
# for i in s:
#     r += 1   # for index position starting from 1.
#     indexNeg = -(l - (r - 1))    # generalise indexing formula for negative index
#     print("s [", indexNeg, "]", end='')
#     print(" --> evaluate to ", i)
# print(s)
# s = "rafik"
# for index in range(len(s)):
#     if s[index] == 'm' or s[index] == 'o':
#         print("there is m and o in S")
# for index in s:
#     if index == 'm' or index == 'o':
#         print("there is m and o in S")
# char = input("enter any char:")
# for char1 in s:
#     if char1 == char :
#         print("FOUND CHARARCTER!!!!! : ", char)
#         break
#     else:
#         print("NO FOUND !!!!!: ",char)
# print("this is second program doing same work as ABOVE in SHORT and EFFIECIENT ")
# if char in s:
#     print("we FOUND the char :", char)
# else:
#     print("NO_FOUND !!!!")
# s1 = input("enter 1 st string:")
# s2 = input("enter 2nd string:")
# for char1 in s1:
#     if char1 in s2:
#         print(char1, end=" ")
# break
# *********** bisection method --> Numerical Technique **********
# x = int(input("enter 1st value of x:"))
# y1 = x ** 2 - 5 * x + 6
# print(y1, end=" ")
# print(" ")
# x = int(input("enter 2nd value of x:"))
# y2 = x ** 2 - 5 * x + 6
# print(y2, end=" ")
epsilon = float(input("enter min epsilon for Accurate result:"))
x1 = 0.1111
x2 = 0.2222
xn = 0.55550
yn = 1.0001


def f(x):
    return x ** 2 - 5. * x + 6


print("I am outside the loop")
# while True:
#     x1 = float(input("input 1st number x1:"))
#     # x = x1
#     # y1 = x1 ** 2 - 5 * x1 + 6
#     print("y1", y1)
#     x2 = float(input("input 2nd number x2:"))
#     # x = x2
#     # y2 = x2 ** 2 - 5 * x2 + 6
#     print("y2", y2)
#     if (f(x1) * f(x2)) < 0:
#         xn = x1 + x2 / 2
#         print("y <0 :", y1 * y2)
#         print("i am in do while loop", end=" ")
#         break
# print("xn  x1  x2= ", xn, x1, x2)
# yn = xn ** 2 - 5 * xn + 6

#
# def check2nditeration(x1, x2, xn):
#     # xn = (x1 + x2) / 2
#     yn = xn ** -5 * xn + 6
#     # y2 = x2** -5 * x2 + 6
#     y1 = x1 ** 2 - 5 * x1 + 6
#     if y1 * yn < 0:
#         xn = (x1 + xn) / 2
#         yn = xn ** -5 * xn + 6
#     else:
#         xn = (x2 + xn) / 2
#         yn = xn ** -5 * xn + 6
#     print("VALUE: ", xn)
#     return yn


noit = 0
flag = 0
while abs(yn) >= epsilon:
    noit += 1
    while flag == 0:
        print("flag value :", flag)
        x1 = float(input("input 1st number x1:"))
        x2 = float(input("input 2nd number x2:"))
        if (f(x1) * f(x2)) < 0:
            flag = 1
            print("flag value 1 :", flag)
            # int(input("enter value 1 to check flag is 1"))
            break
        else:
            print("enter proper value of x1, x2 :")

    print("entered value by user x1, x2 :", x1, x2)
    xn = (x1 + x2) / 2
    print("doing iteration xn:", xn)
    if (f(xn) * f(x1)) < 0:
        print("if checking + /- :", (f(xn) * f(x1)))
        x2 = xn  # this is the key point.
        xn = (xn + x1) / 2
        print("if inside xn :", xn)
        yn = f(xn)
    else:
        print(" else checking + /- :", (f(xn) * f(x2)))
        x1 = xn  # this is the key point.
        xn = (xn + x2) / 2
        print("else inside xn :", xn)
        yn = f(xn)
    print("yn  value:", abs(yn))

print("the best solution of f(xn)  and root  :", yn, xn)
print("no of iteration:", noit)
