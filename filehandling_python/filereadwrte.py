# f = open('ra.txt','w')
# f.write('hi this is 1st line\n')
# f.write(' 2nd line \n')
# n = 0
# while n <3:
#     f.write(f" line no is :{n} and next \n")
#     n = n+1
#
# f.close()
#
# print("direct reading using the read function all text in on one shot:")
# f = open('ra.txt','r')
# txt = f.read()
# print(txt)
# f.close()
#
# print("another method of reading:\n")
# f1 = open('ra.txt','r')
#
# while True:
#     line = f1.readline()
#     print(line)
#     if not line:
#         print("break and last line print:")
#         print(line)
#         break
#

# with open('ra.txt','a') as fileWrite:
#     # file opened in append mode.
#     fileWrite.write("hi this is another method of writting \n")
#     # fileWrite.read()
#     fileWrite.close()
# with open('ra.txt', 'r') as f:
#     # here it is read as complete text in one shot.
#     a = '10'
#     print(int(a))
#     while True:
#         line = f.readline()
#         # print(type(line))
#         line1 = line.split(" ")  # converted into the list.
#         line1.strip(' ')
#         # print(type(line1))
#         list1 = []
#         for l1 in line1:
#             print(l1)
#             lll1 = int(l1)
#             list1.append(l1)
#             # print("l:", type(l1))
#             # l = int(l)
#             print(list1)
#             # print(l1)
#
#         if not line:
#             break
#
# with open('rafi.txt', 'w+') as f:
#     n = 0
#     for i in range(6):
#         n = n + 1
#         txt = input("enter any text and sentences:")
#         f.write(txt)
#         f.write('\t')
#         if (i > 0) & (n % 3 == 0):
#             f.write('\n')
#
#     print("here read function start its work:")
# with open('rafi.txt', 'r') as f1:
#     txt1 = f1.read()
#     print(txt1)
# f.close()



