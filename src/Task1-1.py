from src.graph import *
from collections import deque
import heapq


romania = Graph( ['Or', 'Ne', 'Ze', 'Ia', 'Ar', 'Si', 'Fa',
 'Va', 'Ri', 'Ti', 'Lu', 'Pi', 'Ur', 'Hi',
 'Me', 'Bu', 'Dr', 'Ef', 'Cr', 'Gi'],
[
   ('Or', 'Ze', 71), ('Or', 'Si', 151),
   ('Ne', 'Ia', 87), ('Ze', 'Ar', 75),
   ('Ia', 'Va', 92), ('Ar', 'Si', 140),
   ('Ar', 'Ti', 118), ('Si', 'Fa', 99),
   ('Si', 'Ri', 80), ('Fa', 'Bu', 211),
   ('Va', 'Ur', 142), ('Ri', 'Pi', 97),
   ('Ri', 'Cr', 146), ('Ti', 'Lu', 111),
   ('Lu', 'Me', 70), ('Me', 'Dr', 75),
   ('Dr', 'Cr', 120), ('Cr', 'Pi', 138),
   ('Pi', 'Bu', 101), ('Bu', 'Gi', 90),
   ('Bu', 'Ur', 85), ('Ur', 'Hi', 98),
   ('Hi', 'Ef', 86)
] )
#romania.Print()

def bfs(start, goal, graph):
    start_node = getNode(start, graph.nodes)
    start_node.parent = start_node
    start_node.value = 0
    goal_node = getNode(goal, graph.nodes)

    if start_node == goal_node:
        return start_node
    frontier = deque()
    frontier.append(start_node)
    explored = []

    while frontier:
        node = frontier.popleft()
        explored.append(node)

        for edge in node.edges:
            child = getNode(edge.end.name, graph.nodes)

            if child not in explored:
                if child not in frontier:
                    child.parent = node
                    child.value = node.value + edge.value
                    if goal_node == child:
                        return child
                    frontier.append(child)
    return None

def dfs(start, goal, graph):
    start_node = getNode(start, graph.nodes)
    start_node.parent = start_node
    start_node.value = 0
    goal_node = getNode(goal, graph.nodes)

    if start_node == goal_node:
        return start_node
    frontier = deque()
    frontier.append(start_node)
    explored = []

    while frontier:
        node = frontier.pop()
        explored.append(node)

        for edge in node.edges:
            child = getNode(edge.end.name, graph.nodes)

            if child not in explored:
                if child not in frontier:
                    child.parent = node
                    child.value = node.value + edge.value
                    if goal_node == child:
                        return child
                    frontier.append(child)
    return None

def removeItemFromPQ(q, item):
    returnQueue = []
    heapq.heapify(returnQueue)

    while q:
        i = heapq.heappop(q)
        if i[1] == item:
            break
        heapq.heappush(returnQueue, i)
    return returnQueue

def ucs(start, goal, graph):
    start_node = getNode(start, graph.nodes)
    start_node.parent = start_node
    start_node.value = 0
    goal_node = getNode(goal, graph.nodes)
    explored = []
    frontier = []
    heapq.heapify(frontier)
    heapq.heappush(frontier, (start_node.value, start_node))

    while frontier:
        node = heapq.heappop(frontier)[1]
        if node == goal_node:
            return node
        explored.append(node)

        for edge in node.edges:
            child_node = getNode(edge.end.name, graph.nodes)
            if child_node not in explored and (child_node.value, child_node) not in frontier:
                child_node.parent = node
                child_node.value = node.value + edge.value
                heapq.heappush(frontier, (child_node.value, child_node))
            elif (child_node.value, child_node) in frontier:
                if child_node.value > node.value + edge.value:
                    frontier = removeItemFromPQ(frontier, child_node)
                    child_node.parent = node
                    child_node.value = node.value + edge.value
                    heapq.heappush(frontier, (child_node.value, child_node))
    return None

def printPath(node):
    print("Costs: " + str(node.value))
    path = ""
    while not node.parent == node:
        path = ", " + node.name + path
        node = node.parent
    path = node.name + path
    print(path + "\n")

print("BFS:")
x = bfs("Bu","Ti", romania)
printPath(x)

print("DFS:")
x = dfs("Bu","Ti", romania)
printPath(x)

print("UCS:")
x = ucs("Bu","Ti", romania)
printPath(x)