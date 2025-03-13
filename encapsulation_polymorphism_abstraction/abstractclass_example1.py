from abc import ABC, abstractmethod

# 🔹 Abstract Class: Employee
class Employee(ABC):
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.__salary = salary  # Private attribute (Encapsulation)

    # Getter for salary (Encapsulation)
    def get_salary(self):
        return self.__salary

    # Setter for salary
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary amount!")

    # 🔹 Abstract Method - Must be implemented by all subclasses
    @abstractmethod
    def calculate_bonus(self):
        pass

    # Common method for all employees
    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: {self.get_salary()}")

# 🔹 Concrete Class: Manager (Inherits from Employee)
class Manager(Employee):
    def __init__(self, name, emp_id, salary, team_size):
        super().__init__(name, emp_id, salary)
        self.team_size = team_size  # Additional attribute for Manager

    # Implementing abstract method
    def calculate_bonus(self):
        return self.get_salary() * 0.20  # 20% bonus for managers

    # Overriding display method (Polymorphism)
    def display_info(self):
        super().display_info()
        print(f"Team Size: {self.team_size}")

# 🔹 Concrete Class: Developer (Inherits from Employee)
class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language  # Additional attribute for Developer

    # Implementing abstract method
    def calculate_bonus(self):
        return self.get_salary() * 0.10  # 10% bonus for developers

    # Overriding display method (Polymorphism)
    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

# ✅ Testing the Program
manager1 = Manager("Alice", 101, 80000, 5)
developer1 = Developer("Bob", 201, 60000, "Python")

# Display employee details
print("\nManager Details:")
manager1.display_info()
print(f"Bonus: ${manager1.calculate_bonus()}")

print("\nDeveloper Details:")
developer1.display_info()
print(f"Bonus: ${developer1.calculate_bonus()}")

# Updating Salary using Encapsulation
print("\nUpdating Salary...")
developer1.set_salary(65000)
print(f"Updated Salary: {developer1.get_salary()}")
