import random
print("hello ")
print("enter the number value", 7, 8, 8, sep='!~', end=" 231")
# here 'sep' is seperator for the the objects. give sep = '!~'
# end = " 84" --> it will be at the end of th eprint statements
# print(always)
print("\nRafik")
a = random.randint(1, 100)
print(a)
# a = input("enter a num1:")
# b = input("enter the num2:")
# c = input("enter the operator:")
# if c == +
# print("sum_index is :", int(a)+int(b))
# elif c=='-'
#     print("sum_index is :", int(a) - int(b))
# type(c)
list1 = [1, 2, 3, [4, 6], "rafik", "kalam"]
list2 =[22, 44]
print(list1+list2)
list1[0] = 0
print(list1)
dict1 = {"key1name": "ramu", "key2age": 40}
print(dict1["key1name"] )
print(dict1.keys())
print(dict1.values())
dict1['job'] = "INFN"
print(dict1.keys())
print(dict1.values())
tup = (1, 2, 3, 4, 4)
tup1 = (55, 66)
list1.pop()
list1.append(444)
print(list1)
print(tup+tup1)
