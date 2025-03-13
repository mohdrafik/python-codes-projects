""" method inside a class takes self as an first argument -> this is python convention. 
    when we create a object of a class.
    we call this method using this object --> this object is passed as first argument for the method automatically.
    a
    example we can see:  object(item1) automatically passed to the method calculate_price()

    Example :
    class item:
        def calculate_price(self):
            pass
            
    item1 = item()
    item1.calculate_price<<<<()


 """
class item:
    def __init__(self,name,age,skill =0):
        self.__name= name # name is private attribute.
        self.age = age
        self.skill = skill


    def get_name(self):
        return self.__name
    
        # pass
    def display(self):
        print( f" name : {self.__name} \n age: {self.age} \n skill = {self.skill}")


    
    def set_name(self,newname):
        self.__name = newname
        # print(f"new name set:")


item1 = item("jagan",45,5)
# print(item1.get_name())  # can acces the private member using the getter function.
item1.set_name("Mohammad Rafik")
item1.skill = 20


print(f" {item1.display()}")

# print(item1.age)
# item1.calculate_price()
