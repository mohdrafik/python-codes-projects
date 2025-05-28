# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)
#
#
# n = int(input("enter any integer number: "))
# print("factorial of n :", fact(n))
#
#
# # *** fibonacci series:
# # FIBONACCI
#
# def fib(x):
#     """ assumes x an int >= 0
#         returns Fibonacci of x """
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return fib(x - 1) + fib(x - 2)
#
#
# print("Fibonacci Series: ", fib(10))

dict1 = {"A": "apple", "B": 70, "C ": 100, "D": 500}
print(dict1.keys())
name = ["anna", "luigi", "piet"]
roll_no = [10251, 10252, 10253]
grades = ['A+', 'B', 'C']
dic1 = {}  # empty dictionary
print("the value of the dictionary and value: ")
dict2 = {"anna": [10251, 'A+'], "luigi": [10252, 'B+'], "piet": [10253, 'S']}  # dictionary in dict2.
print(dict2.keys())  # in this way can print the all keys
print(dict2.values())  # in this way can print the all values
print(dict2["anna"])  # similar indexing like list, but here put key value at the place of index.
print(dict2["piet"])
# print(dict2["rafi"])  # this will give error --> because rafi key is not present in the dict2.
# add key and value in dictionary:
dict2["rafik"] = ["MOH", 10258,
                  "A+"]  # NEW ENTRY IN THE DICTIONARY : this new  key and value is added at the ned of the dictionary.
print(dict2["rafik"])
# here can see the added new key and value in dict2
print(dict2.keys())
print(dict2.values())
print(" a", end=' ')
print("   : only space not in next line from the previous print statement")
# test if key in DICTIONARY
if "rafik" in dict2:  # "rafik  "  this will show false so mind the space after the key.
    """  "rafik  "  this will show FALSE so mind the space after the key.
     "rafik"  -> return TRUE  put exactly the same as your key in dictionary """
    print("True")
else:
    print("False")

# delete entry:
print(dict2.keys())  # Evaluate to dict_keys(['anna', 'luigi', 'piet', 'rafik'])
del (dict2["rafik"])
print(dict2.keys())  # --> Now evaluate to  dict_keys(['anna', 'luigi', 'piet'])
# *********** DICTIONARY OPERATIONS: *************
print("DICTIONARY OPERATIONS:")
# get an iterable that acts like a tuple of all keys // * BUT ORDER IS NOT GUARANTEED.

for k in dict2.keys():
    """ printing the key value and in nested for loop  printing the value corresponding the key"""
    print(k, end=': ')
    for val in dict2[k]:
        print(val, end=' ')
    print(" ")

for val in dict2.values():
    print(val)

# ********* DICTIONARY KEYS and VALUES *************
"""
values
• any type (immutable and mutable)
• can be duplicates
• dictionary values can be lists, even other dictionaries!
keys
• must be unique
• immutable type (int, float, string, tuple,bool)
• actually need an object that is hashable, but think of as immutable as all
immutable types are hashable
• careful with float type as a key
# dict3 = {"anna":{"1Y":[10251,2,"Cern"]}, "antonello":[5,10252 ,"cern"], "piet":10 }

"""
print("for dictionary dict3::")
dict3 = {"anna":{"1Y":[10251,2,"Cern"]}, "antonello":[5,10252 ,"cern"], "piet":"10" }
for key in dict3.keys():
    print(key)
    for val in dict3[key]:
        print(val)

# ~ %%%****** ** do some more exercise on the value in dictionary and ;list  form.

# no order to keys or values!  but first element is key and second is value.
d = {4:{1:0}, (1,3):"twelve", 'const':[3.14,2.7,8.44]}
print("keys -> ", end='  ')
print(d.keys())
print("values -> ", end='  ')
print(d.values())

d2 = d  # this is not the new copy, it (d2) is aliasing of d.
print(d2)
d2["ZZZ"] = [10,2,23,55]
print(d)
print(d2)

print(" ****** this is to update the dictionary in programming  :***********  "
      " count the elements in mylist and add them in the dictionary, count the repetetion:  ")
mylist = ["A", "B", "A", "A",10,20,11]
myDic = {}
for x in mylist:
    if x in myDic:
        myDic[x] +=1
    else:
        myDic[x] = 1

print(myDic)

myinfo = {500:124, 501:256, 502:564,503:124}
print(myinfo.items())
""" item() give the content of the dictionary in the list of tuple pair of key and value. """
for key,val in myinfo.items():
    print(f"The key {key} and corresponding value {val}")
cernVisit1 = {"Trip1 ":"3 August 2022","duration":"21 days"}
cernVisit2 = {"Trip2 ":"21 November 2022","duration":"14 days"}
cernVisit3 = {"Trip3 ":"29 december 2022","duration":"7 days"}
cernVisit = {}
cernVisit.update(cernVisit1)
print(cernVisit1.items())
cernVisit3.clear()   # all the item is cleared from the dictionary
print("After clear():",end='')
print(cernVisit3)
cernVisit3 = {"Trip3 ":"29 december 2022","duration":"7 days"}
print(cernVisit3)
cernVisit3.pop("Trip3 ")   # "Trip3 key and value is removed" evaluate to {'duration': '7 days'}
print(cernVisit3)
cernVisit3 = {"Trip3 ":"29 december 2022","duration":"7 days"}
cernVisit3.popitem()  # last item with key an dvalue is removed.
print(cernVisit3)
del(cernVisit3) # cernVisit3 is deleted completely
print(cernVisit3)  # here you can see error: NameError: name 'cernVisit3' is not defined. Did you mean: 'cernVisit1'?
















