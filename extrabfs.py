#Author: Aynura Erejepbaeva
#Date: Mar, 2026
#Purpose: Breadth Search file

from collections import deque
from vertex import Vertex

def breadth_search(start: Vertex, goal: Vertex):
    checked = [start] #list of visited vertices
    queue = deque() #queue for BFS
    queue.append(start)
    path = [] #list to store the final path
    while len(queue) > 0:
        element = queue.popleft()

        if element is goal:
            while not element is None:
                path.append(element)
                element = element.back_pointer
            break

        for neighbor in element.adjacency_list: #eplore neighbors
            if not neighbor in checked:
                checked.append(neighbor)
                neighbor.back_pointer = element
                queue.append(neighbor)
    return path




