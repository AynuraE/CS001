#Author: Aynura Erejepbaeva
#Date: Feb 3, 2025
#Purpose: Pong Game

from cs1lib import * #We need to import certain values from cs1lib
from random import random

HEIGHT = 400 #The height of the window
WIDTH = 400 #The width of the window

paddle1x = 0 #The left paddle x
paddle1y = 0 #The left paddle y

paddle2x = 380 #The right paddle x
paddle2y = 320 #The right paddle y

PADDLE_HEIGHT = 80 #The height of the paddles
PADDLE_WIDTH = 20 #The width of the paddles

OFFSET = 9  #The amount that a paddle moves when it moves
CLEAR = False

BALL_SIZE = 12 #the radius of the ball
ball_x = 200
ball_y = 200
ball_vx = 3 #the minimum velocity of the ball
ball_vy = 3

highlight_frames = 0

LEFTUP = "a" #when I press the key 'a', the top of the left paddle moves up
LEFTDOWN = "z" #when I press the key 'z', the bottom of the left paddle moves down
RIGHTUP = "k" #when I press the key 'k', the top of the right paddle moves up
RIGHTDOWN = "m" #when I press the key 'm', the bottom of the right paddle moves down

a_key = False
z_key = False
k_key = False
m_key = False

game_start = False #starting the game

left_score = 0 #tracking each score
right_score = 0

img = load_image("image.jpg")
right_p = load_image("right paddle.png")
left_p = load_image("left paddle.jpg")
ball_image = load_image("earth.png")

def draw():
    controller()
    ball_movement()
    view()

    #Display the name 'GO BIG GREEN' at the bottom
    set_font_italic()
    set_font_bold()
    draw_text("GO BIG GREEN!", 120, 399)

    draw_image(img, 1, 285) #displaying the house image to mean 'Dartmouth is home'

def view():
    global paddle1x, paddle1y, paddle2x, paddle2y, PADDLE_WIDTH, PADDLE_HEIGHT, BALL_SIZE, ball_x, ball_y, highlight_frames #calling the functions in the global
    clear()
    set_clear_color(0, 1, 0)  # background color is green

    #draw the left paddle in red
    set_fill_color(1, 0, 0)
    draw_rectangle(paddle1x, paddle1y, PADDLE_WIDTH, PADDLE_HEIGHT)
    draw_image(left_p, paddle1x, paddle1y) #displaying the house image to mean 'Dartmouth is home'

    #draw the right paddle in red
    set_fill_color(1, 0, 0)
    draw_image(right_p, paddle2x, paddle2y) #displaying the house image to mean 'Dartmouth is home'

    #draw the ball
    if highlight_frames > 0:
        highlight_frames -= 1
        set_fill_color(random(), random(), random()) #randomize the ball color
        set_clear_color(random(), random(), random()) #randomize the background color
    else:
        set_fill_color(1, 1, 1, 0) #I need alpha to get the transparency
        draw_image(ball_image, ball_x - 12, ball_y - 12)

    draw_circle(ball_x, ball_y, BALL_SIZE)

    #writing the 'Dartmouth' and 'Yale' on the scoreboard
    draw_text("Dartmouth: " + str(left_score), 30, 20)
    draw_text("Yale: " + str(right_score), WIDTH - 100, 20)

def controller(): #paddle movement
    global paddle1x, paddle1y, paddle2x, paddle2y, a_key, z_key, k_key, m_key, OFFSET #calling the functions in the global
    if a_key == True and paddle1y > 0:
        paddle1y = paddle1y - OFFSET
    if z_key == True and paddle1y < HEIGHT - PADDLE_HEIGHT:
        paddle1y = paddle1y + OFFSET
    if k_key == True and paddle2y > 0:
        paddle2y = paddle2y - OFFSET
    if m_key == True and paddle2y < HEIGHT - PADDLE_HEIGHT:
        paddle2y = paddle2y + OFFSET

def ball_movement(): #how the ball moves on the screen
    global BALL_SIZE, ball_x, ball_y, ball_vx, ball_vy, game_start, left_score, right_score, highlight_frames #calling the functions in the global
    if game_start == True:
        if ball_x + BALL_SIZE >= WIDTH: #tracking the scores for left
            left_score += 1
            reset()

        if ball_x - BALL_SIZE <= 0: #tracking the scores for right
            right_score += 1
            reset()

        if ball_y + BALL_SIZE >= HEIGHT: #ball bouncing the verticals
            ball_vy = ball_vy * (-1)

        if ball_y - BALL_SIZE <= 0:
            ball_vy = ball_vy * (-1)

        if ball_x + BALL_SIZE >= WIDTH: #ball bouncing the horizontals
            game_start = False
            reset()

        if ball_x - BALL_SIZE <= 0:
            game_start = False
            reset()

        #Left paddle collision
        if ball_vx < 0 and (ball_x - BALL_SIZE) <= (paddle1x + PADDLE_WIDTH) and paddle1y <= ball_y <= (paddle1y + PADDLE_HEIGHT):
            ball_vx = -ball_vx #so that ball doesn't slither when it touches the edge of the paddles
            ball_x = paddle1x + PADDLE_WIDTH + BALL_SIZE
            highlight_frames += 10

        #Right paddle collision
        if ball_vx > 0 and (ball_x + BALL_SIZE) >= paddle2x and paddle2y <= ball_y <= (paddle2y + PADDLE_HEIGHT):
            ball_vx = -ball_vx #so that ball doesn't slither when it touches the edge of the paddles
            ball_x = paddle2x - BALL_SIZE
            highlight_frames += 10

        ball_y = ball_y + ball_vy #ball moves
        ball_x = ball_x + ball_vx

def reset(): #restarting the game
    global ball_x, ball_y, paddle1y, paddle2y, ball_vx, ball_vy
    ball_x = 200
    ball_y = 200
    paddle1y = 0
    paddle2y = 320
    ball_vx = 3
    ball_vy = 3

    ball_vx += random() * 5
    ball_vy += random() * 5

    if random() < 0.5:
        ball_vx = -ball_vx
    if random() < 0.5:
        ball_vy = -ball_vy

def my_kpress(key):  #which keyboard key to use
    global a_key, z_key, k_key, m_key, q_key, game_start
    if (key == LEFTUP):
        a_key = True
    if (key == LEFTDOWN):
        z_key = True
    if (key == RIGHTUP):
        k_key = True
    if (key == RIGHTDOWN):
        m_key = True
    if (key == 'q'):
        cs1_quit()
    if (key == " "):
        game_start=True

def key_release(key): #I want the paddle to stop when I'm not pressing the keys
    global a_key, z_key, k_key, m_key, q_key
    if (key == 'a'):
        a_key = False
    if (key == 'z'):
        z_key = False
    if (key == 'k'):
        k_key = False
    if (key == 'm'):
        m_key = False

reset()
## somewhere in a drawing function called by start_graphics:
start_graphics(draw, width = WIDTH, height= HEIGHT, key_press=my_kpress, key_release=key_release) #calling the function