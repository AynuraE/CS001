#Author: Aynura Erejepbaeva
#Date: Jan 21, 2026
#Purpose: String Art (need to use a string in a different place every time. Second time it comes, it will draw a new line)

from cs1lib import *

x = 0
y = 0
WIN_SIZE = 400 #window size
OFFSET = 20 #how wide the distance between each point
CLEAR = False

def main_draw():
    global x, y #to be updated each time, we use a global value
    global CLEAR

    if not CLEAR:
        clear()
        CLEAR = True #I don't want the lines to be erased after an action

    set_stroke_color(0, 1, 0) #stroke is green
    set_stroke_width(6) #it should be visible within the line
    draw_point(x, y)

    set_stroke_color(0, 0, 1) #line is blue
    set_stroke_width(2) #how thin the line is
    draw_line(x,y,y, WIN_SIZE - x)

    operation()

def operation(): #helper function
    global x, y #to be updated each time, we use a global value

    if y == 0 and x < WIN_SIZE:
     x = x + OFFSET #this is the top side
    elif x == WIN_SIZE and y < WIN_SIZE:
     y = y + OFFSET #this is the right side
    elif y == WIN_SIZE and x >= OFFSET:
     x = x - OFFSET #this is the bottom side
    elif y >= OFFSET and x == 0:
     y = y - OFFSET #this is the left side

start_graphics(main_draw, width=400, height=400)