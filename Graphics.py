from cs1lib import *

x = 10
y = 10
def main_draw():  # Must not take any parameters
    global x, y
    # set background color to black
    set_clear_color(0, 0, 0)
    clear()

    #Draw a circle
    set_fill_color(1, 0, 0)
    draw_circle(x,y, 50)
    x = x + 5
    y = y + 5

start_graphics(main_draw)