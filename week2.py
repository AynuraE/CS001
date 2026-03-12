#Author: Aynura
#Date: Jan 12, 2026
# Purpose: Week1 recitation: Bulls eye (use laptop)

#Problem:
# 1. Using cs1lib.py write a program that will draw a
# bullseye target as shown by the TA.
# 2. Define variables for position and size of the bullseye target.

from Week2.cs1lib import * #pulling the code from the library

def my_draw():
    x = 200
    y = 200

    #Background color is black
    set_fill_color(0, 0, 0)

    #Circles --> eyes
    set_fill_color(0, 0, 1)
    draw_circle(x, y, 130)

    set_fill_color(0, 1, 0)
    draw_circle(x, y, 80)

    set_fill_color(1, 0, 0) #first circle is blue
    draw_circle(x, y, 40)

start_graphics(my_draw)



