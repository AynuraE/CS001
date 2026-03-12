#Author: Aynura Erejepbaeva
#Date: Feb, 2026
#Purpose: Target driver

from cs1lib import *
from random import randint
from Week6.target import Target


t1 = Target(100, 150, 60)
print(t1)
t1.update(5, 5)

def mydraw():
    # set background
    set_clear_color(1, 1, 1)
    clear()

    t1.draw()

start_graphics(mydraw)
