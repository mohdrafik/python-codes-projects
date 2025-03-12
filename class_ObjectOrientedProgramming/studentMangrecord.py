class Student:
    school_name = "Greenwood High"  # Class variable

    def __init__(self, name, grade, marks):
        """Initialize student details"""
        self.name = name
        self.grade = grade
        self.marks = marks

    @classmethod
    def change_school(cls, new_name):
        """Update school name"""
        cls.school_name = new_name

    @staticmethod
    def is_passed(marks):
        """Check if the student passed"""
        return marks >= 50

    def display_info(self):
        """Display student details"""
        print(f"School: {Student.school_name}")
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"Marks: {self.marks}")
        print(f"Passed: {'Yes' if self.is_passed(self.marks) else 'No'}\n")

#   Create students
student1 = Student("Jake", 10, 85)
student2 = Student("Emily", 9, 45)

#   Display student info
student1.display_info()
student2.display_info()

#   Change school name
Student.change_school("Sunrise Academy")

#   Verify the change in school name
print("\nAfter School Name Change:")
student1.display_info()
student2.display_info()
