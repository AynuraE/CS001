#Purpose: Circle driver (Demo __str__ method, interaction with cs1lib)

from cs1lib import *
from Week6.circle import Circle

c1 = Circle(100, 100, 50, 1, 1, 0)

def mydraw():
    #set background
    set_clear_color(1, 1, 1)
    clear()

    c1.update(1, 1)
    c1.draw()

start_graphics(mydraw)