def print_tuple(tup):
    for i in tup:
        print(i, end=' ')
    print(" ")


# tup1 = range(1, 8)
tup1 = (1, 2, 3, 4, 3, 4, 4, 55, 25)
print("tup is :", tup1)
# for i in tup1:
#     print(i, end='  ')
print_tuple(tup1)
# print(" ")  # just for new line
print("tup2 is :", tup1)
print(tup1.count(4))
# tup3 = tup1[3:]
tup3 = tup1[3:]
print_tuple(tup3)
print(tup3)
print()
print(max(tup1))
print(len(tup1))
print("now we see the index of 55:")
print(tup1.index(55))

