import readline

file = open('myfile.dat','w')
file.write('my name is Moh Rafik\n')
file.write('I work in poliba Bari\n')
file.write('Now I will work in the CNR STIIMA\n')
file.close()

file = open('myfile.dat','r')
n =0
# while True:
print(file.read())
# if not readline:
#     pass
# else:
#     # print(readline)
#     print(file.read())

file.close()