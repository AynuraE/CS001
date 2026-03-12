#Author: Aynura Erejepbaeva
#Date: Mar, 2026
#Purpose: Map Plot file

#Draws the Dartmouth map

from cs1lib import *
from vertex import Vertex
from load_graph import create_vertex_dictionary
#Importing necessary functions
from bfs import breadth_search

#loads the file
vertex_dict = create_vertex_dictionary("dartmouth_graph.txt")

new_list = []
created_list = []

selected_vertex = None

def my_mpress(mx, my): #mouse for mouse press
    global selected_vertex
    for i in vertex_dict.values():
        if i.is_on_vertex(mx, my):
            selected_vertex = i
            break

def my_release(mx, my): #function for mouse release
    global selected_vertex, created_list
    if not selected_vertex is None:
        if selected_vertex.is_on_vertex(mx, my):
            new_list.append(selected_vertex)
            if len(new_list) % 2 == 0:
                created_list = breadth_search(new_list[-2], new_list[-1])

def draw():
    global image
    draw_image(image, 0, 0) #draw the background map
    set_font_size(22)

    for key in vertex_dict: #draws all vertices and edges
        value = vertex_dict[key]
        value.draw_vertex(0, 0, 1) #draws vertices in blue
        value.draw_all_edges(0, 0, 1) #draws edges (lines) in blue
        for i in range(len(created_list)):
            created_list[i].draw_vertex(1, 0, 0) #draws BFS path in red
            if i != 0:
               created_list[i].draw_edge(1, 0, 0, created_list[i-1])  # draws edge (lines)
            set_stroke_color(0.25, 0, 0.5)

            if i == 0 or i == len(created_list) - 1:
              draw_text(created_list[i].name, created_list[i].x, created_list[i].y-4)


image = load_image("dartmouth_map.png") #loads the map image
start_graphics(draw, width=1012, height=811, mouse_press=my_mpress, mouse_release=my_release) #we're calling draw function and passing in the width and height of the image.