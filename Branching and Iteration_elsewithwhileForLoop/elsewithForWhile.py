# i = 0
# while i <= 5:
#     print(i)
#     i = i+1
# else:
#     print("else with for:", "no  i")
#
# i = 0
# while i <= 5:
#     print(i)
#     i = i+1
#     if i == 3:
#         break
# else:
#     print("else with for:", "no  i")


while True:
    n = int(input("guess a number:"))
    if n == 10:
        print("you win !")
        break
    else:
        print("try Again!")
