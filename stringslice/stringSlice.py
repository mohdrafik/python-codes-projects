# text1 = "hi all, \" study hard amke some plan \" "
# print(text1)
# text2 = 'hi all, study hard and make some plan '
# print(text2)
# print("for next line \n")
# text3 =''' hi all
# study hard and "make some" plan"
# and execute the plan '''
# print(text3)
# # print(text1[0])
# # print(text1[1])
# # for char in name :
# #     name = "RAFIK"
# #     print(char)
# ....  new program line ...........string slicing ......
# nm = "moh rafik"
# ln1 = len(nm)
# print(ln1)
# print(nm[0:ln1])   # not includes ln1 i.e. = 9th character
# print(nm[:ln1])
# print(nm[0:])
# print(nm[:])
# print(nm[-3:ln1])
# # print(nm[-1:-8])
# .day13................. some function use to manipulate of string .............
str1 = "raffia is bar is"
print(str1.endswith("bar"))  # it will return true because str1 ends with bari mind space also be carefull
print(str1.endswith("bar "))  # false --> because of space
# we can use this in conditional statements (if/while/continue...)
print(str1.count("b"))  # count a in the str1.
aa1 = str1.split(" ")  # it split the str1 string in list when it finds the space between them.
print(len(aa1))
print(str1.split(" "))
print(str1.center(50))
nm2 = 'dear piet, iam going to cern'
# capitalize.str1()
print(str1.endswith("ar", 8, 9))
print(str1.find("is"))   # will give the index of a in str1 if found.otherwise return -1.
print(str1.index("is"))  # this will also return index if found otherwise through exception
print(str1.isalnum())  # alphanumerical a-z A-Z, 0-9
str2 = "canvasy tmera"
print(str2.isalnum())
print(str2.islower())
str3 = "  "   # using tab and space both
print(str3.isspace())
str3 = " hi I am going to CERN\n"
print(str3.isprintable())   # return False because str3 contain \n (slash n ) which is not printable characater.
str4 = "To kill a Mocking bird"
print(str4.istitle())
print(str3.swapcase())    # convert lower to upper and upper to lower.
str1 = "He is a word of main"
print(str1.title())  # it will make upper case all the letter.













