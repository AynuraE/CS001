#Purpose: Circle class definition

from cs1lib import *
class Circle:
    def __init__(self, gx, gy, gsize, \
                 r=0, g=1, b=0):
        self.x = gx
        self.y = gy
        self.radius = gsize
        self.r = r
        self.g = g
        self.b = b

    def update(self, vx, vy):
        self.x = self.x + vx
        self.y = self.y + vy
        print("Circle update")

    def draw(self):
        set_fill_color(self.r, self.g, self.b)
        draw_circle(self.x, self.y, self.radius)
        print("Circle draw")

    def __str__(self):#only self as parameter
        #must return a string
        print("In circle __str__")
        return str(self.x) + "," + str(self.y)



