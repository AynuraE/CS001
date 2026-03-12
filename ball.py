#Author: Aynura Erejepbaeva
#Date: Feb, 2026
#Purpose: Ball class definition

from random import randint

class Ball:
    def __init__(self, gx, gy, gsize):
        self.x = gx
        self.y = gy
        self.size = gsize
        self.vx = self.size//10
        self.vy = randint(2, 5)
        self.r = 0
        self.g = 1
        self.b = 0
        print("Self:", self)

    def update(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        print("Self update:", self)