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

def bfs(start, graph, goal):
    explored = []
    queue2 = queue.Queue()

    queue2.put(getNode(start, graph.nodes))


    while not queue2.empty():
        node = queue2.get()
        if node not in explored:
            explored.append(node)
            for neighbour in node.edges:
                queue2.put(getNode(neighbour.end.name, graph.nodes))
    return explored

x=bfs("Ti",romania)
for xs in x:
    print(xs.name)

# def breadth_first_search(graph, start, end):
#     explored = []
#     queue2 = queue.Queue()
#     queue2.put(getNode(start, graph.nodes))
#
#     while not queue2.empty():
#         node = queue2.get()
#         print(node.name)
#         if node not in explored:
#             explored.append(node)
#             for neighbour in node.edges:
#                 neighbourNode = getNode(neighbour.end.name, graph.nodes);
#                 if neighbourNode not in explored:
#                     queue2.put(neighbourNode)
#
#     return




#x = breadth_first_search(romania, "Ti","Ti")
#action: abzugehende dinger


#
# def breadthFirstSearch(start, goal):
#     frontier = queue.Queue()
#     frontier.put(getNode(start,romania.nodes))
#     visited = []
#     costs = 0
#
#     while(not frontier.empty()):
#         node = frontier.get()
#         visited.append(node.name)
#
#         for edge in node.edges:
#             if(edge.end.name not in visited):
#                 if(edge.end.name == goal): print("jawohl")
#                 frontier.put(edge.end)
#     return None
#
# breadthFirstSearch("Bu","Ti")
#
