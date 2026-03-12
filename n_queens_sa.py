#Author: Aynura Erejepbaeva
#Date: Feb, 2026
#Purpose: N-queens validation problem solution
from stringprep import c22_specials

from cs1lib import *
from random import randint

WIN_SIZE = 500
N = 5
CELL_SIZE = WIN_SIZE // N
first = True
end = False
board_lol = []

#Create NxN board with empty cells (all cells are false)
def initialize_empty_board():
    i = 0
    while i < N:
        board_lol.append([])
        j = 0
        while j < N:
            board_lol[i].append(False)
            j = j + 1

        i = i + 1

#Capture mouse location and find the cell and flip the true-false flag

def my_mpress(mx, my):
    col = mx // CELL_SIZE
    row = my // CELL_SIZE

    board_lol[row][col] = not board_lol[row][col]

#The function that takes a list of lists representation of the board and draw the chessboard. It draws placed queens as red circles.

def draw_board(glol, n):
    # clear background
    set_clear_color(1, 1, 1)
    clear()

    if len(glol) != n:
        print("Wrong outer list length", n)
        return
    sqr_width = WIN_SIZE // n
    i = 0
    while i < n:
        if len(glol[i]) != n:
            print("Wrong inner list length")
            return
        j = 0
        while j < n:
            if (j+i) % 2 == 0:
                set_fill_color(1, 1, 1)
            else:
                set_fill_color(0.5, 0.5, 0.5)

            sqr_x = i * sqr_width
            sqr_y = j * sqr_width
            draw_rectangle(sqr_y, sqr_x, sqr_width, sqr_width)

            #Check if that cell has a queen and draw a circle in red.
            if glol[i][j] == True:
                set_fill_color(0.9, 0, 0)
                draw_circle(sqr_y+sqr_width//2, sqr_x+sqr_width//2, sqr_width//10)

            j = j +1
        i = i + 1

#This function takes a list of lists representing the N*N chessboard with N queens placed randomly on board and returns True if no two queens attach each other. Otherwise, it returns False.

def check_board(glol):
    #ADD YOUR CODE HERE
    #You may define helper functions for this function
    i = 0
    N = len(glol)
    queens = []
    while i < N:
        j = 0
        while j < N:
            if glol[i][j] == True: #there is a queen at position i, j
                coordinate = [i, j]
                queens.append(coordinate)

            j = j + 1
        i = i + 1

    return find_all(queens)
#Description: i equals to rows and j equals to columns. N represents where the Queens located in my list/chessboard. My code identifies where True is located within rows and columns, and saves it into memory of my new list.

def find_all(queens):
    for queen1 in range(0, len(queens)-1):
        for queen2 in range(queen1 + 1, len(queens)):
            attacking = attack(queens[queen1], queens[queen2])
            if attacking:
                return False
    return True
#Description: I'm trying to find if queens are attacking each other

def attack(q1, q2):
    r1 = q1[0]
    c1 = q1[1]
    r2 = q2[0]
    c2 = q2[1]
    if (r1 == r2) or (c1 == c2) or (r1 - c1 == r2 - c2) or (r1 + c1 == r2 + c2):
        return True
#Description: I'm trying to calculate in which conditions queens cannot attack each other.

#Main draw function
def my_draw():
    global first, end
    if first:
        set_clear_color(1, 1, 1)
        clear()
        first = False

    check = check_board(board_lol)
    end = not check #end is true when check_board returns False

    draw_board(board_lol, N)
    if end:
        # clear()
        # set_clear_color(1, 1, 1)
        draw_board(board_lol, N)
        set_font_size(50)
        draw_text("The End", 150, 250)

initialize_empty_board()
start_graphics(my_draw, width=WIN_SIZE, height=WIN_SIZE, mouse_press=my_mpress)