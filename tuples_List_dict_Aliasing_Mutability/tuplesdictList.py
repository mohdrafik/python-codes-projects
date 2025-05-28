# atuple = (25, "rafik", 55.52, True)
# atuple[0]
# len(atuple)
# print(" 0th index value of the tuple:", atuple[0], "and length of the tuple: ", len(atuple))
# print(atuple + (
#     10, 20, 30))  # --> evaluate to (25, 'rafik', 55.52, True, 10, 20, 30) :   concatenation of the tuple is allowed.
# print(atuple[1:2])  # --> evaluate to  ('rafik',) -> extra comma means tuple with single value
# # only (" rafik")  --> it is string.
# # x = range(1, 5, 2)
# # for i in x:
# #     print(i, x)
# # ********** swap the value  **********
# # ********* using simple method *******
# (x, y) = (10, 20)
# print("Before swapping :--> ", "x val:", x, "Y val:", y)
# temp = x
# x = y
# y = temp
# print("After  swapping :--> ", "x val:", x, "Y val:", y)
#
# print("  ")
# # ********** swap the value  **********
# # ********* using TUPLE *******
# print("Before swapping :--> ", "x val:", x, "Y val:", y)
# (x, y) = (y, x)
# print("After  swapping :--> ", "x val:", x, "Y val:", y)
#
# tuple can be used to return more than one values from the function:

# def get_data(atuple):
#     num = ()
#     words = ()
#     for t in atuple:
#         num = num + (t[0],)
#         if t[1] not in words:
#             # print(t[1])
#             words = words + (t[1],)
#     min_n = min(num)
#     max_n = max(num)
#     unique_words = len(words)
#     # print(words)
#     return min_n, max_n, unique_words
#
#
# t1 = ((20, "ram"), (25, "satish"), (40, "rafik"))
# # tuple of tuple.
# (Min_age, Max_age, num_people) = get_data(t1)
# print("Minimum aged person :", Min_age, "Max aged person :", Max_age, "Total number of persons:", num_people)
#
# L1 = [1, 2, 3]
# print(L1)
# L1.extend([10, 20, 30])
# # L1 is mutated here with extend() function.
# print(L1)

# L = [1, 2, 3, 4, 5, 6]

#
# def sum_all(list1):
#     sum1 = 0
#     for el in list1:
#         sum1 += el
#     return sum1
#
#
# Total_sum = sum_all(L)
# print("sum of all elements of list : ", Total_sum)

# sum_index = 0
# for i in range(len(L)):
#     sum_index = sum_index + L[i]
#
# print("sum of all elements : ", sum_index)

# L = [1, 2, 3, 4]
# print(L)  # --> [1, 2, 3, 4]
# L.append(55)  # --> mutate the list L. L now [1, 2, 3, 4, 55]
# print(L)  # -->  output of print [1, 2, 3, 4, 55]
# L.extend([10, 20, 30])  # --> L is mutated
# print(L)  # --> [1, 2, 3, 4, 55, 10, 20, 30]
#
# L1 = [6, 0, 9, 5]  # L1 is unchanged
# L2 = [1, 2]  # L2 is unchanged
# L3 = L1 + L2
# print(L3)  # output L3 => [6, 0, 9, 5, 1, 2]
# del (L3[5])
# print(L3)
# del (L3[0])
# print(L3)
# # remove element at end of list with L.pop(), returns the removed element
# L3.pop()
# print(L3)

# remove a specific element with L.remove(element)
# it remove the elements by its value, looks for the element in the list and remove it.
# if elements occurs multiple times, its delete it first occurred value.
# if element is not in the list then give error.
# L = [2,6,1,6,7,9,0,3]
# L.remove(6)
# print(L)

# s = "R6<5 ec e"  # → s is a string
# list(s)  # →   returns ['R', '6', '<', '5', ' ', 'e', 'c', ' ', 'e']
# print(list(s))
# s.split('<')  # → returns ['R6', '5 ec e']
# print(s.split('<'))
# (s.split())  # → returns['R6<5', 'ec', 'e']
# print(s.split())
# L = ['j', 'u', 'm']  # → L is a list
# ''.join(L)  # → returns "jum"
# print(''.join(L))
# '_'.join(L)  # → returns "j_u_m"
# print('_'.join(L))

# aliases and mutability
# l1 =['apple', 'banana', 'orange']
# print(l1)   # ['apple', 'banana', 'orange']
# l2=l1
# l2.append('guava')
# print(l1)   # ['apple', 'banana', 'orange', 'guava']
# print(l2)   # ['apple', 'banana', 'orange', 'guava']

# use of sort and sorted function.
List = ['orange', 'apple', 'banana']
sortList = List.sort()
print(sortList)   # None
print(List)   # ['apple', 'banana', 'orange']

name = ['sharif', 'janu', 'nasib']
sortedList = sorted(name)
print(sortedList)

# 
# def remove_dups(L1, L2):
#     for e in L1:
#         if e in L2:
#             L1.remove(e)