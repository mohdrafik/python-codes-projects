import csv
class Item:
    pay_rate = 0.8
    all = []

    def __init__(self,name:str,price:float,qunantity =0):

        assert price >=0, "price shlold be positive or zero"
        assert qunantity >= 0, " quantity shold be whole numbers"

        # Assign to the self object
        self.name =  name
        self.price = price
        self.quantity = qunantity

        # action to be execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price*self.quantity
    def apply_discount(self):
       return self.price* self.pay_rate

    def __repr__(self):   # representation magic method 
        # return f"Item('{self.name}',{self.price}, {self.quantity}) "
        return f"('{self.name}',{self.price}, {self.quantity}) "

    @classmethod
    def instance_fromcsv(cls):
        with open('item.csv','r') as f:
            reader = csv.DictReader(f)
            item = list(reader)

        for item in item:
            print(item)
    # @staticmethod

# item1 = Item("phone",100,1)
# item2 = Item("headphone",900,1)
# item3 = Item("tablet",1000,1)
# item4 = Item("bottle",500,1)
# item5 = Item("laptops",500,1)

# print(f" the item1 price {item1.calculate_total_price()} and discounted price:{item1.apply_discount()}")
# print(Item.all)

# for items in Item.all:
#     print(f" item name: {items.name} and its price: {items.price}")

# print(Item.all)
Item.instance_fromcsv()