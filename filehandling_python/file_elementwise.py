# f = open('rafi.txt', 'r')
# n = 0
#
#
# def calcu(l1):
#     x = []
#     for val in l1:
#         val1 = int(val)
#         val1 = val1 + 3
#         x.append(val1)
#     print(x)
#
#
# while True:
#     n = n + 1
#     line = f.readline()
#     print(line)
#     if n == 1:
#         print("here type of data in by readline:", type(line))
#     line1 = line.split(",")
#     # print("after split type of line1::", type(line1), len(line1))
#     calcu(line1)
#     # line.split(",")
#     # print(line1)
#     if not line:
#         break

# with open('rafi.txt','r+') as f:
#     # f.readline()
#     for line11 in f:
#         print(line11,end='')

# ****** read all the lines in list use list(f) or f.readlines()
# with open('rafik.txt','w+') as f:
#     # list(f)
#     # print(list(f))
#
#     value = ('the answer', 42)
#     s = str(value)  # convert the tuple to string
#     f.write(s)
# import json
# x = [1, 'simple', 'list']
# json.dumps(x)
# # '[1, "simple", "list"]'
# print(json.dumps(x))
# print(100/7)
# with open('rafik.txt','r+') as f:
#     f.seek(6+1) # it will shift the file pointer by the 10 bytes forward (+10) or backward (-10).
#     tx1t = f.read(12) # here size = 5, it read 5 bytes (5 character)
#     print(tx1t)
#
# with open('rafik.txt','a+') as f:
#     f.write("hi this is current line:\n")
#
# with open('rafik.txt','r+') as f1:
#     txt = f1.read()
#     print(txt)
#     f1.seek(200)   # this will set the pointer at 201byte position  or Go to the 201th byte in the file
#     print(f1.read(20))
#     print(f1.tell())  # this is used to tell the position of the pointer in file.where the file pointer points. it returns a integer.
#
#
#
