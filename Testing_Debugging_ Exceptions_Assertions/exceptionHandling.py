# # *** program case for exceptions:
# list = [1, 2, 3, 4, 5]
# for i in range(len(list)):
#     print(list[i])
#
# try:
#     2/0  # this is not defined in any except condition. then only body of the except: executed.
#     # 'a' / 4
#     list[6]  # give error :-->  IndexError: list index out of range
#     int(list)  # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
#     a  # without define the object just wrote the object name
#     'a' / 4
#     z = len([2, 3, 4, 5])  # syntax error.
#     print(z)
# except IndexError:
#     print(" IndexError: index order index given in list index argument is out of order.")
# except TypeError:
#     print("type error: ")
# except NameError:
#     print("referencing a non-existing variable")
# except TypeError:
#     print(" mixing data types without coercion ")
# except SyntaxError:
#     print("SyntaxError: check syntax")
# except:
#     print("something went wrong:")

### the above code will run evenafter having the error.

# can write seperate error and seperate exception:
#
# try:
#
#     'a' / 4
# except TypeError:
#     print("type error")
# #
#
# try:
#     a = int(input("enter the num:"))
#     b = int(input("enter another num:"))
#     a/b
# except:
#     print("wrong user input,remove that bug.")
#
# # another example of the exception handling:

# try:
#     a = int(input("enter a number:"))
#     b = int(input("enter another number:"))
#     print("a/b =  ",a/b)
#     print("a+b  = ",a+b)
# except ValueError:
#     print("could not convert a number: , ValueError: operand is ok but entered number is not valid")
# except ZeroDivisionError:
#     print("can't divide by zero:")
# except:
#     """ for all other errors except these two above  errors."""
#     print("something different error is there! ")


# when try clause body don't produce any exception then body of the else clause execute.
# if try body produce the exception then except clause body is executed.
# try:
#     a = int(input("enter any number:"))
#     b = int(input("enter 2nd number:"))
#     print("a/b = ", a / b)
# except:
#     print(" an exception occurred in try clause:")
# else:
#     print("no exception: else statement is executed when no exception occur in try clause")


# ***  finally:
"""   
1. finally CLAUSE BODY is always executed even after the  break and continue statement.
  no matter it has been inside the function after the return statement also. 
2. useful for clean-up code that should be run no matter what else happened (e.g. close a file).
"""
# def sub():
#     try:
#         list =[1,2,3,4,5]
#         a = list[3]
#         b = list[4]
#         if a>b :
#             return 1
#             # print(" hi i am returning 1.")
#     except:
#         print("hi I am in except when exception occurs")
#         return 0
#
#     finally:
#         print(" THIS STATEMENT, I am in finally body")
#     """  but finally body is always executed even if after the return statement """
#
#     print(" I am always want to be executed")
#     """ this will not be executed because it is written after the return statement of the function. """
#
#
# x = sub()
# print(" function output is = ", x)

# signal error condition. raise an exception.

""" exception as flow control, 
 Generally when an exception occur in try body , error is produced by the python exceptional handler
  and handeled by the except: body statement.
 but in raise an exception, we can raise our own exception when some desired result is not occured.

syntax:

raise <exception name>  (<arguments>)

raise ValueError ("some thing went wrong.")   
 
 """

# def findratio(L1, L2):
#     ratio = []
#     for index in range(len(L1)):
#         try:
#             ratio.append(L1[index] / L2[index])
#         except ZeroDivisionError:
#             ratio.append(float("NaN"))  # at the place of division by zero put NaN.
#         except:
#             raise ValueError("get ratio called with bad argument")
#     return ratio
#
#
# L3 = [4, 5, 7, 8, 9, 10]
# L4 = [2, 5, 8, 0, 3, 2]
# print("divide list ; Ratio = ", findratio(L3, L4))
# print(findratio(L3, L4))


# l1 =[]
# l1.append([[1],[5],[7]])
# print(l1)
# L1 = [10, 2, 13]
#
#
# def avg(grade):
#     return sum(grade) / len(grade)
#
# print(avg(L1))

# suppose we have a list of student and their three marks in a subject assignment.
class_list = [[['moh', 'Rafik'], [80, 69, 76]], [['hoti', 'lal'], [45, 68, 56]], [['jumma', 'khan'], [45, 89, 78]],
              [['hasan', 'saeed'], []]]


def get_statistics(class_test) :
    new_statistics = []
    for elem in class_test:
        new_statistics.append([elem[0], elem[1], avg(elem[1])])  # elem[0] evaluate to the name and elem[1] to grades.

    return new_statistics


def avg(grades):
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        print(" warning  some student have no garde data")
        """  # OPTION 1: FLAG THE ERROR BY PRINTING A MESSAGE only as like above.
         
        otherwise  OPTION 2: CHANGE THE POLICY,  decide that a student with no grades gets a zero
         """
        return 0.0

print(get_statistics(class_list))    # invoke the function.

