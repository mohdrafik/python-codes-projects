import pandas as pd
import numpy as np

grade_dict = {"GRADE":['S','A','B','C','D','E','F'], "GRADE_POINT":[10,9,8,7,6,5,0]}
grade_dict.keys()
grade_dict.values()
gcdata = pd.DataFrame(grade_dict) 
gcdata.set_index(["GRADE"],inplace=True)

# l = input("enter any letter :")  # it is for testing the gradepoint output corresponding to the grade obtained.
# gcdata.loc[l,'GRADE_POINT']
# enter any letter :S
# output = 10
credit_scoredUpto =[]


credit =[]
grade_obtained =[]
score =[]
Total_creditEarned = 0

print(f"credit    grade_obtained    score    TotalcreditEarned")
for i in range(7):
    inC = int(input("enter the credit:"))
    ingrade_obtained = input("input grade obtained:")
    credit.append(inC)
    grade_obtained.append(ingrade_obtained)
    grade_point = gcdata.loc[ingrade_obtained,"GRADE_POINT"]
    Total_creditEarned  += credit[i]*grade_point
    score.append(credit[i]*grade_point)
    if i ==max(range(6)):
        SPI = Total_creditEarned/sum(credit)
    print(f"{credit[i]}    {grade_obtained[i]}    {score[i]}    {Total_creditEarned}    ")  

print("SPI -->", SPI)    
        
print(f"credit    grade_obtained    score ")    
for (c,g,s) in zip(credit,grade_obtained,score):
    print(f"{c}        {g}               {s}    ")  
    
print("SPI -->", SPI)       
#credit_earneduptosem.append(Total_creditEarned)    



credit_scoredUpto.append(148)
credit_scoredUpto.append(182)
credit_scoredUpto