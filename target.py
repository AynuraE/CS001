#Author: Aynura Erejepbaeva
#Date: Feb, 2026
#Purpose: Target class definition

from Week6.circle import Circle

class Target:
    def __init__(self, x, y, size):
        self.c1 = Circle(x, y, size//3, 1, 0, 0) #red circle
        self.c2 = Circle(x, y, size*2//3, 0, 1, 0) #green circle
        self.c3 = Circle(x, y, size, 0, 0, 1) #blue circle

    def update(self, vx, vy):
        print("Target update")
        self.c1.update(vx, vy)
        self.c2.update(vx, vy)
        self.c3.update(vx, vy)


    def draw(self):
        print("Target draw")
        self.c3.draw()
        self.c2.draw()
        self.c1.draw()

    def __str__(self):
        s = str(self.c1) + ":" + str(self.c2) + ":" + str(self.c3)
        return s