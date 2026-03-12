from cs1lib import *

width = 1024
height = 768
x = 0
dx = 5

def sunny():
    global x, dx
    set_fill_color(0, 1, 1)
    clear()
    set_clear_color(0, 1, 1) #background, sky
    set_fill_color(0, 0.5, 0) #grass
    draw_rectangle(0, 500, width, height-500)
    set_fill_color(1, 1, 0) #sun
    draw_circle(x, 100, 100)
    if x > width + 50 or x < -50:
        dx = -dx
    x = x + dx

start_graphics(sunny, width=width, height=height)