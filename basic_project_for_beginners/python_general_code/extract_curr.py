# with open('readcurr.txt','r') as f:
#     # d = f.readli()
#     count =0
#     # print(d)
#     for line11 in f.readline():
#         # print
#         count = count+1
#         print(line11)
#     # print(count)
#         if count ==2:
#             break
#     # if (~(count == 1)):
    #     val = line.split(',')[0]
    # # print(data)
    #     print(val)

current = '-3.656463E-14A,+7.150091E+03,+5.120000E+02'
dc = current.split(',')[0].rstrip('A')
print(dc)
print(type(dc))

dc = float(current.split(',')[0].rstrip('A'))
print(dc)
print(type(dc))
# actualcurrent = dc[0]
# print(actualcurrent)
# valtcurr = float(actualcurrent.rstrip('A'))
# print(valtcurr)
# print(type(valtcurr))





