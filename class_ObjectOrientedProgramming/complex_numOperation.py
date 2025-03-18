# # class OperateOncomplex_Num:
# #     @staticmethod
# #     def enterComplexNum():
# #         realComp = float(input("enter real part of complex num:"))
# #         ImagComp = float(input("enter Imaginary part of complex num:"))


#     # pass
#     def __init__(self,num1:float,num2:float):
#         self.num1 = num1
#         self.num2 = num2
#         # pass
    
#     # def add(self,):
#     def display(self):
#         return f"real part {}"
# userinput = input()
# print(userinput.split())

class rafik:
    def __init__(self,num1,num2):
        self.r1 =num1
        self.r2 = num2

    # def __add__(self,n2):
    #     return f" sum : {self.r1 + n2.r1} and numbers : {self.r2 + n2.r2} and complex number is ----->: {self.r1 + n2.r1} + {self.r2 + n2.r2}i " 

    def __add__(self,n2):
        return f" sum : {self.r1 + n2} and numbers : {self.r2 +n2} and complex number is ----->: {self.r1 + n2} + {self.r2 + n2}i " 
    
    # def add(self,n2):
    #     return f" sum : {self.r1 + n2} and numbers : {self.r2 +n2} and complex number is ----->: {self.r1 + n2} + {self.r2 + n2}i " 
   
n1 = rafik(20,30)
# n2  = rafik(4,5)
n2 = 10
# xx = n1.add(n2)
# print(xx)
# result = n1.__add__(n2)
# print(result)

result = n1+n2
print(result)
