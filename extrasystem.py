#Author: Aynura Erejepbaeva
#Date: Feb, 2026
#Purpose: System class

from cs1lib import *
from body import Body
from math import * #importing from cs1lib, body, and math (which is a global file)

G = 6.67384e-11 #When computing acceleration, I need this value

#This is the System class file that works with Body objects. It updates their motion and draws them on the screen.
class System: #class called System
    def __init__(self, body_list):
        #This is a list of Body objects in the simulation
        self.body_list = body_list

    def draw(self, cx, cy, pixels_per_meter): #draw methods for both classes
        for body in self.body_list:
            body.draw(cx, cy, pixels_per_meter)

    def update(self, timestep):
        for body in self.body_list:
            a_x, a_y = self.compute_acceleration(body)
            body.update_velocity(a_x, a_y, timestep)
            body.update_position(timestep)

    def compute_acceleration(self, n):
        # Initialize total acceleration properties to zero
        a_x = 0
        a_y = 0
        for body in self.body_list:
            if n != body:
                dx = body.x - n.x
                dy = body.y - n.y
                dis = sqrt((dx**2)+(dy**2))
                a = (G * body.mass)/(dis**2)
                a_x = a_x + a * (dx/dis)
                a_y = a_y + a * (dy/dis)
        #Return total acceleration 
        return a_x, a_y