# ...............day14 if-else_conditional ...........
# a = int(input("enter ticket amount:"))
# if (a <= 350):
#     print("you can book a ticket")
#     print("this is good")
# else:
#     print("wait for some days:")
#     print("you should be careful next time")
# print("yes")  # this is out of the else block. without indentation

# ..................2nd example.....................
marks = int(input("enter your marks :"))
if (marks >= 75):
    print("passed with honor")
elif marks >= 60:
    print("passed with First dIvision")
elif marks >= 45:
    print("PASSED WITH 2ND DIV")
elif marks >= 33:
    print("PASSED WITH 3RD DIV")
else:
    while marks:
        print("!!!! FAIL !!!!!")
        marks = marks % 5     # this statement considered INSIDE the while loop.
        print("just check how mark decrease marks", marks)  # # this statement considered OUTSIDE the while loop.
        marks = marks - 1  # this statement considered INSIDE the while loop.
    print("marks", marks)   # # this statement considered OUTSIDE the while loop.
