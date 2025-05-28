"""
creating instance of the class.
data attributes of an instance (object) are called instance variables
don’t provide argument for self, Python does this automatically
 """


class coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        """here self use to refer to any instance.
        which is defined e.g. c(instance/object)  = coordinate(3, 4) -> here self refer to c itself.
         or origin (instance/object) = coordinate(0, 0) -> here self refer to origin itself.
         """
        x_diff_square = (self.x - other.x) ** 2
        y_diff_square = (self.y - other.y) ** 2
        return (x_diff_square + y_diff_square) ** 0.5

    def __str__(self):
        return "< " + str(self.x) + "," + str(self.y) + " >"

    def __add__(self, other):
        add1 = self.x + other.x
        # print("addition = ", 310 + 500)
        return add1


c = coordinate(6, 8)
origin = coordinate(0, 1)
# print(c.y)
# print(origin.y)
print("Distance between c and origin = ", origin.distance(c))
print("Distance between c and origin = ", c.distance(origin))  # this wil also give the same value.
print("Distance between c and origin = ", coordinate.distance(c, origin))
print(c)
print(type(c))
print(coordinate)
print(type(coordinate))
print(c.y + origin.y)
