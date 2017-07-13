'''
The University of Chicago
Master Program of Computer Science (MPCS)
2015-2016
Programming Placement Exam Problem
Python2 Solution for
"Staying Connected"

Problem Description: https://uchicago.kattis.com/problems/uchicagoplacement.connected

Author: Lei Mao
Date: 7/13/2017
Last Revised: 7/13/2017
'''

import sys

fhand = sys.stdin
lines = fhand.readlines()

# The number of vertices
V = int(lines[0].strip())
# The number of edges
E = int(lines[1].strip())

# Visited state of vertices
vertices = [False] * V
# Edge information
edges = list()
for line in lines[2:]:
    [vertex_1, vertex_2] = line.split(' ')
    edges.append((int(vertex_1), int(vertex_2)))

# Depth-first search algorithm to explore an entire connected components in graph.
def dfs(edges, root_vertex):
    global vertices
    vertices[root_vertex] = True
    for edge in edges:
        if edge[0] == root_vertex or edge[1] == root_vertex:
            if edge[0] == root_vertex and vertices[edge[1]] == False:
                vertices[edge[1]] = True
                dfs(edges = edges, root_vertex = edge[1])
            elif edge[1] == root_vertex and vertices[edge[0]] == False:
                vertices[edge[0]] = True
                dfs(edges = edges, root_vertex = edge[0])
    return


# The count of connnected components
cc_count = 0
# The count of connnected components that have more than two nodes
for (i, edge) in enumerate(edges):
    if vertices[edge[0]] == False or vertices[edge[1]] == False:
        cc_count += 1
        dfs(edges = edges[i:], root_vertex = edge[0])
# Add the count of connnected components that have single node
cc_count += (V - sum(vertices))

print(cc_count)