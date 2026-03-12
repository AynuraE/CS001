#Author: Aynura Erejepbaeva
#Date: Mar, 2026
#Purpose: Adventure!

from vertex import Vertex

def parse_line(line):
    section_split = line.split("|")
    vertex_name = section_split[0].strip()

    adjacent_vertices = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    text = section_split[2].strip()

    return vertex_name, adjacent, text


def load_story(filename):

    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for l in file:

        # if this is a line in the correct format:
        if len(l.split("|")) == 3:
            vertex_name, adjacent_vertices, text = parse_line(l)

            print("vertex " + vertex_name)
            print(" adjacent:  " + str(adjacent_vertices))
            print(" text:  " + text)
            new_vertex = Vertex(adjacent_vertices, text)
            vertex_dict[vertex_name] = new_vertex
        # create a graph vertex here and add it to the dictionary

    file.close()

    return vertex_dict

def play_game(filename):
    vertex_dict = load_story(filename)
    current_vertex = vertex_dict["START"]
    while True:
        print(current_vertex.data)
        if current_vertex.adjacency_list == []:
            break
        x = input("Choose a, b, or c: ")

        index = ord(x) - ord("a")

        next_vertex_name = current_vertex.adjacency_list[index]
        current_vertex = vertex_dict[next_vertex_name]

play_game("story.txt")
