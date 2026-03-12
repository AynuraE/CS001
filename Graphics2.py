#Purpose: Chasing siblings example
from cs1lib import *

smallx = 200
smally = 200
ssize = 50

bigx = 200
bigy = 200
bsize = 100

mpressed = False #This boolean variable remembers if mouse is being pressed

def draw_eye(x, y, size):
    #outer circle
    enable_stroke()
    set_stroke_color(0, 0, 0)
    set_stroke_width(1)
    set_fill_color(1, 1, 1)
    draw_circle(x, y, size)

    #inner circle
    set_fill_color(0, 0, 0)
    draw_circle(x, y-size//2, size//2)

def draw_smiley(x, y, size, r, g, b): #Must not take any parameters
    #draw face
    disable_stroke()
    set_fill_color(r, g, b)
    draw_circle(x, y, size)

    #draw mouth
    enable_stroke()
    set_stroke_width(size*0.05)
    set_stroke_color(1, 0, 0)
    x1 = x - size*0.3
    y1 = y + size*0.3
    x2 = x + size*0.3
    y2 = y + size*0.3
    draw_line(x1, y1, x2, y2)

    #draw eyes
    left_x = x - size*0.3
    left_y = y - size*0.3
    eye_size = size*0.2
    draw_eye(left_x, left_y, eye_size)

    right_x = x + size*0.3
    right_y = y - size*0.3
    draw_eye(right_x, right_y, eye_size)

def mydraw():
    #set background
    set_clear_color(1, 1, 1)
    clear()

    #draw the small smiley
    draw_smiley(smallx, smally, ssize, 1, 1, 0)

    #draw the big smiley
    draw_smiley(bigx, bigy, bsize, 0, 1, 1)

def my_mpress(mx, my):
    global mpressed
    mpressed = True

    #Code to make the small smiley to chase the big one
    # global smallx, smally, bigx, bigy
    # smallx = bigx
    # smally = bigy
    # bigx = mx
    # bigy = my

def my_mmove(mx, my):
    global bigx, bigy
    if mpressed == True:
        bigx = mx
        bigy = my

def my_mrelease(mx, my):
    global mpressed
    mpressed = False

def my_kpress(value):
    print(value)

start_graphics(mydraw, mouse_press=my_mpress, mouse_move=my_mmove, \
               mouse_release=my_mrelease, key_press=my_kpress)

