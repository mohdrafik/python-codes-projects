class Book:
    def __init__(self,author,subject):
        self.author = author
        self.subject = subject
        # pass
    def __str__(self):
        # pass
        return f"Book author : {self.author} and Subject :{self.subject}"
    
    def __del__(self):
        print(f" b1 object is deleted :{self.author}")
    
b1 = Book("abdul kalam","science")
print(b1)
del b1  # after deleteing the object b1:
print(b1) # after deleteing the object b1, we got the following message
"""  
Traceback (most recent call last):
  File "e:\python_programs\special_methods_in_OOPS\del_dundermethod.py", line 16, in <module>
    print(b1)
NameError: name 'b1' is not defined
"""