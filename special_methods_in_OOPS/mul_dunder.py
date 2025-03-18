class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __mul__(self,other):
        if isinstance(other,Vector):
            new_x = self.x * other.x
            new_y = self.y * other.y
            return  new_x + new_y
        else:
            raise TypeError(" unsupported other object for *")
    
v1 = Vector(2,3)
v2 = Vector(4,5)

v3 = v1*v2
print(v3)  # output 23
