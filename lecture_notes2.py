#Author: Aynura Erejepbaeva
#Date: Feb, 2026
#Purpose: Physical simulation of a bouncing ball
from cs1lib import *

FRAMERATE = 40
TIMESTEP = 1 / FRAMERATE

WIN_H = 400
PIXEL_PER_METER = 20 #This is like the scale of a world map

RADIUS = 1

x = 0 #meters
y = 10 #meters

VX = 2 #meters/sec
vy = 0 #m/s

g = -9.8  #meters/sec^2

def update():
    global x, y, vy

    #Updating position
    x = x + VX * TIMESTEP
    y = y + vy * TIMESTEP

    #Updating velocity
    if (y - RADIUS) <= 0:
        vy = -vy
    else:
        vy = vy + g * TIMESTEP

def draw():
    pixel_x = x * PIXEL_PER_METER
    pixel_y = WIN_H - y * PIXEL_PER_METER
    pixel_radius = RADIUS * PIXEL_PER_METER

    set_fill_color(1, 0, 1)
    draw_circle(pixel_x, pixel_y, pixel_radius)


def my_draw():
    #set background
    set_clear_color(1, 1, 1)
    clear()

    draw()
    update()

start_graphics(my_draw, framerate=FRAMERATE, width=WIN_H, height=WIN_H)

