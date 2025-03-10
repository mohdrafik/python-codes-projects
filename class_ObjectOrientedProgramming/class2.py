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
    def calculate_price(self):
        print("thsis is method")
        pass
            

item1 = item()
item1.calculate_price()
