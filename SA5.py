#Author: Aynura Erejepbaeva
#Date: Jan 26, 2026
#Purpose: Chalkboard
from cs1lib import * #we need to import certain values from cs1lib

old_x = 0 #starting point
old_y = 0

curr_x = 0 #second point of the line
curr_y = 0

CLEAR = False

mpressed = False #This boolean variable remembers if mouse is being pressed

red = False
green = False
blue = False
yellow = False

def main_draw():
    global old_x, old_y, curr_x, curr_y, red, green, blue, yellow
    global CLEAR

    if not CLEAR:
        set_clear_color(0, 0, 0)  # set background color for black
        clear()
        CLEAR = True #I don't want the lines to be erased after an action

    set_stroke_width(2) #how thin the line is
    set_stroke_color(1, 1, 1)

    if red == True:
        set_stroke_color(1, 0, 0)
    if green == True:
        set_stroke_color(0, 1, 0)
    if blue == True:
        set_stroke_color(0, 0, 1)
    if yellow == True:
        set_stroke_color(1, 1, 0)

    draw_line(old_x, old_y, curr_x, curr_y)
    old_x = curr_x
    old_y = curr_y

def my_mpress(mx, my):
    global mpressed
    global curr_x, curr_y, old_x, old_y
    curr_x, curr_y = mx, my
    old_x, old_y = mx, my
    mpressed = True

def my_mmove(mx, my): #my mouse connecting points
    global curr_x, curr_y
    if mpressed == True:
        curr_x = mx
        curr_y = my

def my_mrelease(mx, my): #what happens after I let go of the mouse
    global mpressed
    mpressed = False

def my_kpress(key): #which keyboard key to use for the drawing
    global red, green, blue, yellow
    if (key == 'r'):
        red = True
        green, blue, yellow = False, False, False
    if (key == 'g'):
        green = True
        red, blue, yellow = False, False, False
    if (key == 'b'):
        blue = True
        red, green, yellow = False, False, False
    if (key == 'y'):
        yellow = True
        red, green, blue= False, False, False

start_graphics(main_draw, mouse_press=my_mpress, mouse_move=my_mmove, mouse_release=my_mrelease, key_press=my_kpress)