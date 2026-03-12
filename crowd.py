from cs1lib import *
from random import uniform
from face import Face

class Crowd:
    def __init__(self, size):
        self.size = size
        self.crowd_list = []

        rand_x = uniform(0,1)
        rand_y = uniform(0,1)
        face1 = Face(rand_x, rand_y, size)
        self.crowd_list = [face1]

    def lookat(self, lx, ly):
        face1 = self.crowd_list[0]
        face1.lookat(lx,ly)

    def draw(self):
        face1 = self.crowd_list[0]
        face1.draw()

