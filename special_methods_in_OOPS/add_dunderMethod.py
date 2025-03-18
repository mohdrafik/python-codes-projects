# dunder Method: double under score method.
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        if isinstance(other,Vector):
            new_x = self.x +other.x
            new_y = self.y +other.y
            return Vector(new_x,new_y)
        else:
            raise TypeError(" unsupported other object for + ")
    def __str__(self):
        return f"Object :{self.x},{self.y}"
    

vector1 = Vector(3,5)  
vector2 = Vector(5,9)
res = vector1 + vector2 

print(vector1) 
print(vector2) 
print(res)
