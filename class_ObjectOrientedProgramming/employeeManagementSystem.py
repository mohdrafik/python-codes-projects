class Employee:
    company_name = "TechKbridge"
    def __init__(self,name:str, position:str,salary:int):

        if not self.is_valid_salary(salary):
            raise ValueError("Salary must be a positive number.")

        self.name = name
        # assert name!=" ",'position can not be a empty'
        self.position = position
        self.salary = salary

    @classmethod
    def change_company_name(cls,new_name):
        cls.company_name = new_name
        print(f"name is updated to the {new_name}")

    @staticmethod
    def is_valid_salary(salary):
        if salary <= 0:
            print("Error: Salary must be greater than zero.")
            return False
        return True
    
    
    def display_info(self):
    
        print(f" company name: --> {Employee.company_name}\n employee name: --> {self.name}\nposition:--> {self.position} \n salary :--> {self.salary} ")
        
        # print(f"salary :--> {self.salary}")

e1= Employee("jumma","manager",1000)
e1.change_company_name("INFN")
e2= Employee("abdul","doctor",2000)

e2.display_info()
        
"""
.strip() -->
What Does name.strip() Do?
The .strip() method removes leading and trailing spaces from a string.
If the name is empty or only contains spaces, .strip() will return an empty string ("").
How if not name.strip() Works
The condition if not name.strip() checks whether the stripped string is empty ("").
If the name is empty or contains only spaces, it raises a ValueError.
"""