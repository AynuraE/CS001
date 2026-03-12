#Author: Aynura Erejepbaeva
#Date: Feb, 2026
#Purpose: Body class

from cs1lib import * #importing from cs1lib

#Body class represents physical objects with various properties. Each Body can draw itself and update its motion over time
class Body: #class X (name of the class)
    def __init__(self, mass, x, y, v_x, v_y, image_path): #The Body class will have x, y, v_x, v_y instance variables, at least, to represent the location and velocity of the Body.
        #We need self in every method
        self.x = x     #position of the body, x, in meters
        self.y = y     #position of the body, y, in meters
        self.v_x = v_x #velocity for x
        self.v_y = v_y #velocity for y
        self.mass = mass # mass of the body
        self.image_path = load_image(image_path) #for loading images
        self.angle = 0

    def draw(self, cx, cy, pixels_per_meter): #draw methods for both classes
        # From simulation coordinates (meters) into pixel coordinates
        # Multiply by pixels_per_meter to scale the distance
        ppixels_x = self.x * pixels_per_meter #updating pixels
        ppixels_y = self.y * pixels_per_meter
        s_x = cx + ppixels_x
        s_y = cy - ppixels_y
        self.angle = self.angle + 3 #rotating the body by 3 degrees
        draw_image(self.image_path, s_x, s_y, self.image_path.width()/2, self.image_path.height()/2, self.angle)

    def update_position(self, timestep): #update_postion and update_velocity methods for the location and velocity in Body class.
        self.x = self.x + self.v_x * timestep #updating the position for x
        self.y = self.y + self.v_y * timestep #updating the position for y

    def update_velocity(self, ax, ay, timestep): #update_postion and update_velocity methods for the location and velocity in Body class.
        #Updating velocity based on acceleration
        self.v_x = self.v_x + ax * timestep
        self.v_y = self.v_y + ay * timestep