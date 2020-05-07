from src.graph import *
import queue

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
    explored = []
    q = queue.Queue()
    path = [0, start]
    q.put(path)

    while not q.empty():
        path = q.get()
        node_name = path[-1]
        if node_name not in explored:
            explored.append(node_name)
            node = getNode(node_name, graph.nodes)
            for edge in node.edges:
                path1 = path.copy()
                path1[0] += edge.value
                path1.append(edge.end.name)
                if edge.end.name == goal:
                   return path1
                q.put(path1);
    return None

def dfs(start, goal, graph):
    explored = []
    q = queue.LifoQueue()
    path = [0, start]
    q.put(path)

    while not q.empty():
        path = q.get()
        node_name = path[-1]
        if node_name not in explored:
            explored.append(node_name)
            node = getNode(node_name, graph.nodes)
            for edge in node.edges:
                path1 = path.copy()
                path1[0] += edge.value
                path1.append(edge.end.name)
                if edge.end.name == goal:
                   return path1
                q.put(path1);
    return None

def ucs(start, goal, graph):
    explored = []
    q = queue.PriorityQueue()
    path = [0, start]
    q.put(path)

    while not q.empty():
        path = q.get()
        node_name = path[-1]
        if node_name not in explored:
            explored.append(node_name)
            node = getNode(node_name, graph.nodes)
            for edge in node.edges:
                path1 = path.copy()
                path1[0] += edge.value
                path1.append(edge.end.name)
                if edge.end.name == goal:
                   return path1
                q.put(path1);
    return None

print("BFS:")
print(bfs("Bu","Ti", romania))
print("DFS:")
print(dfs("Bu","Ti", romania))
print("ucs:")
print(ucs("Bu","Ti", romania))