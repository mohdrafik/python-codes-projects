# # Base class (Parent)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# # Hierarchical Inheritance
# class Student(Person):  # Student inherits from Person
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

#     def display_student(self):
#         print(f"Student ID: {self.student_id}")

# class Teacher(Person):  # Teacher inherits from Person
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject

#     def display_teacher(self):
#         print(f"Teaches: {self.subject}")

# # Hybrid Inheritance: Teaching Assistant (inherits from both Student & Teacher)
# class TeachingAssistant(Student, Teacher):  
#     def __init__(self, name, age, student_id, subject):
#         # Call constructors of both Student and Teacher
#         super().__init__(name, age, student_id)
#         Teacher.__init__(name, age, subject)
#         # self.subject = subject
        
#         # super().__init__(name, age, student_id)
#         # super().__init__(name, age, subject)

#         # self.name= name
#         # self.age= age
#         # self.student_id = student_id
#         # self.subject = subject


#     def display_ta(self):
#         print(f"Teaching Assistant: {self.name}")
#         print(f"Student ID: {self.student_id}, Teaching Subject: {self.subject}")

# # Creating objects
# ta = TeachingAssistant("Alice", 25, "S12345", "Computer Science")

# # Calling methods
# ta.display()        # From Person class
# ta.display_student() # From Student class
# ta.display_teacher() # From Teacher class
# ta.display_ta()     # From TeachingAssistant class

# Base class (Parent)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Hierarchical Inheritance
class Student(Person):  # Student inherits from Person
    def __init__(self, name, age, student_id):
        Person.__init__(self, name, age)  # Explicitly call Person's __init__
        self.student_id = student_id

    def display_student(self):
        print(f"Student ID: {self.student_id}")

class Teacher(Person):  # Teacher inherits from Person
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)  # Explicitly call Person's __init__
        self.subject = subject

    def display_teacher(self):
        print(f"Teaches: {self.subject}")

#  Multiple inheritance
class TeachingAssistant(Student, Teacher):  
    def __init__(self, name, age, student_id, subject):
        Student.__init__(self, name, age, student_id)  # Call Student's init
        Teacher.__init__(self, name, age, subject)  # Call Teacher's init

    def display_ta(self):
        print(f"Teaching Assistant: {self.name}")
        print(f"Student ID: {self.student_id}, Teaching Subject: {self.subject}")

# Creating object
ta = TeachingAssistant("Alice", 25, "S12345", "Computer Science")

# Calling methods
ta.display()        # From Person class
ta.display_student() # From Student class
ta.display_teacher() # From Teacher class
ta.display_ta()     # From TeachingAssistant class

