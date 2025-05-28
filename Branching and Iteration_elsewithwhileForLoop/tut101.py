# x = range(6)
# for n in x:
#     print(n, end=' ')
# print(" ")
# x = range(1, 5)
# for n in x:
#     print(n, end=' ')
# print('')
# x = range(1, 6, 2)
# for n in x:
#     print("n from range:", n)
# -----------------day16------------------
# x = int(input("enter any num: "))
# match x:
#     case 1:
#         print("num is one")
#
#     case 2:
#         print("num is 2")
#
#     case _ if x != 4:
#         print(x, "x is not 2")
#     case _:
#         print(x, "is default x")
# for loop -----------------day17------------------
# list1 = ["red", "green", "blue"]
# for color in list1:
#     print(color, end=' ')
#     print(" ")
#     for i in color:
#         print(i)
# while loop -----------------day18------------------
# i = 0
# while i < 5:
#     i = int(input("enter the i value:"))
#     print(i, end=' ')
#     print(" ")
#     i = i + 1
# emulate do while loop in python example : do this example
while True:
    number = int(input("enter the positive num: "))
    print(number)
    if not number > 0:
        break
# here before the if condition it will print number at least
# one time evenif condition is not true (while True)
# like do while  if condition is true it again print and so on




# break and continue statement  -----------------day19------------------
# for i in range(12):
#     print("5 x", i + 1, " = ", 5 * (i + 1))
#     if i == 9:
#         break
# print("this is outside of the loop")

for i in range(12):
    if i % 2 != 0:
        continue
    print(i)  # print all th even number using the continue statement

print("this is outside of the loop")
