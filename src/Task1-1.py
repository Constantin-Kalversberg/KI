from math import sqrt

from src.graph import *

import queue
class Node:
    def __init__(self, position):
        self.parent = 0
        self.cost = float('inf')
        self.position = position
        self.symbol = "*"



    def __lt__(self, other):
        return 0




field = [[Node((y, x)) for x in range(20)] for y in range(20)]
field[0][19].symbol = "G"
for y in range(11):
    field[y][16].symbol = "X"

for y in range(10):
    field[10+y][9].symbol = "X"

for x in range(5):
    field[10][4+x].symbol = "X"

def printMap(field):
    for row in field:
        out = ""
        for column in row:
            out += column.symbol
        print(out)


printMap(field)

def removeFromPq(q, item):
    returnQueue = queue.PriorityQueue()
    while not q.empty():
        x = q.get()
        if(not x[1] == item):
            #returnQueue.put((x[0], x[1]))
            returnQueue.put(x)
    return returnQueue

def isInPQ(q, item):
    returnValue = 0
    while not q.empty:
       if(q.get()[1] == item):
          returnValue = 1
    return returnValue

def AStar():
    open = queue.PriorityQueue()
    closed = []
    #initalize
    field[19][0].cost = 0
    field[19][0].parent = field[19][0]
    open.put((sqrt((19-0)**2+(0-19)**2), field[19][0]))


    while not open.empty():
        s = open.get()[1]
        if(s.symbol == "G"):
            return s
        if s not in closed:
            closed.append(s)

        neighbours = []

        if(s.position[0]+1 < len(field)):
            neighbours.append(field[s.position[0]+1][s.position[1]])
        if(s.position[1]+1 < len(field[0])):
            neighbours.append(field[s.position[0]][s.position[1]+1])
        if(s.position[0]-1 >= 0):
            neighbours.append(field[s.position[0]-1][s.position[1]])
        if(s.position[1]-1 >= 0):
            neighbours.append(field[s.position[0]][s.position[1]-1])

        for neighbour in neighbours:
            if not neighbour.symbol == "X":
                if neighbour not in closed:
                    if isInPQ(open, neighbour):
                        neighbour.cost = float('inf')
                        neighbour.parent = 0

                #Update Vertex
                if s.cost + 1 < neighbour.cost:
                    neighbour.cost = s.cost + 1
                    neighbour.parent = s
                    if isInPQ(open, neighbour):
                        open = removeFromPq(open, neighbour)
                    open.put(((neighbour.cost+sqrt((neighbour.position[0] - 0)**2 + (neighbour.position[1] - 19)**2)),neighbour))

    return "Nein"





s =AStar()

i=0
while not s == s.parent:
    i+=1
    s.symbol= "A"
    s = s.parent

print(i)
printMap(field)

asdf = queue.PriorityQueue()
node = Node((3,2))
node2 = Node((3,2))

asdf.put((2,node))
asdf.put((2,node))
asdf.put((2,node))
asdf.put((2,node))
asdf = removeFromPq(asdf, node)
isInPQ(asdf, node)
asdf.put((2,node))
asdf.put((2,node))
asdf.put((2,node))



#
# romania = Graph( ['Or', 'Ne', 'Ze', 'Ia', 'Ar', 'Si', 'Fa',
#  'Va', 'Ri', 'Ti', 'Lu', 'Pi', 'Ur', 'Hi',
#  'Me', 'Bu', 'Dr', 'Ef', 'Cr', 'Gi'],
# [
#    ('Or', 'Ze', 71), ('Or', 'Si', 151),
#    ('Ne', 'Ia', 87), ('Ze', 'Ar', 75),
#    ('Ia', 'Va', 92), ('Ar', 'Si', 140),
#    ('Ar', 'Ti', 118), ('Si', 'Fa', 99),
#    ('Si', 'Ri', 80), ('Fa', 'Bu', 211),
#    ('Va', 'Ur', 142), ('Ri', 'Pi', 97),
#    ('Ri', 'Cr', 146), ('Ti', 'Lu', 111),
#    ('Lu', 'Me', 70), ('Me', 'Dr', 75),
#    ('Dr', 'Cr', 120), ('Cr', 'Pi', 138),
#    ('Pi', 'Bu', 101), ('Bu', 'Gi', 90),
#    ('Bu', 'Ur', 85), ('Ur', 'Hi', 98),
#    ('Hi', 'Ef', 86)
# ] )
# #romania.Print()
#
# def bfs(start, goal, graph):
#     explored = []
#     q = queue.Queue()
#     path = [0, start]
#     q.put(path)
#
#     while not q.empty():
#         path = q.get()
#         node_name = path[-1]
#         if node_name not in explored:
#             explored.append(node_name)
#             node = getNode(node_name, graph.nodes)
#             for edge in node.edges:
#                 path1 = path.copy()
#                 path1[0] += edge.value
#                 path1.append(edge.end.name)
#                 if edge.end.name == goal:
#                    return path1
#                 q.put(path1);
#     return None
#
# def dfs(start, goal, graph):
#     explored = []
#     q = queue.LifoQueue()
#     path = [0, start]
#     q.put(path)
#
#     while not q.empty():
#         path = q.get()
#         node_name = path[-1]
#         if node_name not in explored:
#             explored.append(node_name)
#             node = getNode(node_name, graph.nodes)
#             for edge in node.edges:
#                 path1 = path.copy()
#                 path1[0] += edge.value
#                 path1.append(edge.end.name)
#                 if edge.end.name == goal:
#                    return path1
#                 q.put(path1);
#     return None
#
# def ucs(start, goal, graph):
#     explored = []
#     q = queue.PriorityQueue()
#     path = [0, start]
#     q.put(path)
#
#     while not q.empty():
#         path = q.get()
#         node_name = path[-1]
#         if node_name not in explored:
#             explored.append(node_name)
#             node = getNode(node_name, graph.nodes)
#             for edge in node.edges:
#                 path1 = path.copy()
#                 path1[0] += edge.value
#                 path1.append(edge.end.name)
#                 if edge.end.name == goal:
#                    return path1
#                 q.put(path1);
#     return None
#
# print("BFS:")
# print(bfs("Bu","Ti", romania))
# print("DFS:")
# print(dfs("Bu","Ti", romania))
# print("ucs:")
# print(ucs("Bu","Ti", romania))