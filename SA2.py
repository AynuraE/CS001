#Author: Aynura Erejepbaeva
#Date: Jan 13, 2026
#Purpose: Bookcover
#Function to draw a snowman

# 8 shapes (you may use draw same shape multiple times)
# 2 lines
# your name

from cs1lib import *

def draw():
    x = 400
    y = 400

    #draw a black background
    set_fill_color(0, 0, 0)

    #draw the shine
    disable_stroke()
    set_fill_color(1, 1, 0)  # set fill color to yellow
    draw_triangle(160, 20, 240, 70, 240, 90)

    #draw a planet
    disable_stroke()
    set_fill_color(1, 1, 0) # yellow
    draw_circle(200, 50, 25)

    #draw a lawn
    disable_stroke()
    set_fill_color(0, .5, 0)  # dark green
    draw_circle(200, 400, 100)

    #Display name
    enable_stroke()
    set_fill_color(1, 0, 0,) #red
    draw_text("AYNURA", 170, 390)

    #little hat
    enable_stroke()
    set_stroke_width(100 * 0.05)
    set_stroke_color(1, 0, 0)
    draw_line(190, 210, 170, 190)

    draw_body()
    my_stick()

def draw_body():
    #head
    disable_stroke()
    set_fill_color(1, 1, 1) #white
    draw_circle(190, 210, 15)

    #body
    disable_stroke()
    set_fill_color(1, 1, 1) #white
    draw_circle(190, 240, 20)

def my_stick():
    #draws a stick
    enable_stroke()
    set_stroke_width(100 * 0.05) #red
    set_stroke_color(1, 0, 0)
    draw_line(180, 170, 160, 320)

    disable_stroke() #white
    set_fill_color(1, 1, 1)
    draw_circle(190, 285, 30)

start_graphics(draw) #calls my function