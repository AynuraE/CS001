#Author: Aynura Erejepbaeva
#Date: Mar, 2026
#Purpose: Vertex file

from cs1lib import *

#Vertex holds the information about each vertex in the graph.

class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.adjacency_list = [] #its name, its x and y locations on the map, and a Python list to hold the references of adjacent vertices in the graph.
        self.back_pointer = None

    def draw_vertex(self,  r, g, b):
        set_fill_color(r, g, b)
        set_stroke_color(0, 0, 0, 0)
        #draw a small circle at the vertex location
        draw_circle(self.x, self.y, 5)

    def draw_edge(self, r, g, b, other_vertex):
        set_stroke_color(r,g,b)
        #This draws a line between A and B
        draw_line(self.x, self.y, other_vertex.x, other_vertex.y)

    def draw_all_edges(self, r, g, b):
        #This connects one vertex with the rest of the vertices
        for other in self.adjacency_list:
            self.draw_edge(r, g, b, other)

    def is_on_vertex(self, x, y):
        if abs(self.x - x) <= 5:
            if abs(self.y - y) <= 5:
                return True
        return False

    def __str__(self):
        #Adjacent vertices separated by commas
        v_str = ""
        for x in range(len(self.adjacency_list)):
            v_str = v_str + self.adjacency_list[x].name
            if x < len(self.adjacency_list) - 1:
                v_str = v_str + ", "
        #return with the format required. Converts x and y to integers
        return self.name + "; " + "Location: " + str(self.x) + ", " + str(self.y) + "; " + "Adjacent vertices: " + v_str