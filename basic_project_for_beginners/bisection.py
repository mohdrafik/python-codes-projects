epsilon = float(input("enter min epsilon for Accurate result:"))
x1 = 0.1111
x2 = 0.2222
xn = 0.55550
yn = 1.0001

def f(x):
    return x ** 2 - 5. * x + 6

print("I am outside the loop")
noit = 0   # to count the no of iteration
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

