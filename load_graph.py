#Author: Aynura Erejepbaeva
#Date: Mar, 2026
#Purpose: Load Graph file

from vertex import Vertex

def parse_line(line):
    section_split = line.split(";") #Splits the lines with semicolons
    adjacent_vertices = section_split[1].strip().split(",") #gets the adjacent vertex names
    xy = section_split[2].strip().split(",")
    x = int(xy[0]) #converting a string to an integer
    y = int(xy[1]) #converting a string to an integer

    name = section_split[0].strip() #gets the vertex name

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    return name, adjacent, x, y

def create_vertex_dictionary(filename): # takes the name of the input file as a parameter
    vertex_dict = {} #this dictionary maps vertex names to vertex objects

    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for l in file:

        # if this is a line in the correct format:
        if len(l.split(";")) == 3:
            name, adjacent_vertices, x, y = parse_line(l)

            new_vertex = Vertex(name, x, y)
            vertex_dict[name] = new_vertex
        # create a graph vertex here and add it to the dictionary

    file.close()

    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for line in file:
        if len(line.split(";")) == 3:
            name, adjacent_vertices, x, y = parse_line(line)
            curr_vertex = vertex_dict[name] #Find the current vertex object
            for v_str in adjacent_vertices:
                curr_vertex.adjacency_list.append(vertex_dict[v_str])

    file.close()

    return vertex_dict #This returns the dictionary that has now all vertices