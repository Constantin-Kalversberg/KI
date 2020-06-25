from math import sqrt
import heapq

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

def removeItemFromPQ(q, item):
    returnQueue = []
    heapq.heapify(returnQueue)

    while q:
        i = heapq.heappop(q)
        if i[1] == item:
            break
        heapq.heappush(returnQueue, i)
    return returnQueue

def AStar():
    open = []
    heapq.heapify(open)
    closed = []

    #initalize
    field[19][0].cost = 0
    field[19][0].parent = field[19][0]
    heapq.heappush(open,(sqrt((19-0)**2+(0-19)**2), field[19][0]))

    while open:
        s = heapq.heappop(open)[1]
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
                    if neighbour in open:
                        neighbour.cost = float('inf')
                        neighbour.parent = 0
                #Update Vertex
                if s.cost + 1 < neighbour.cost:
                    neighbour.cost = s.cost + 1
                    neighbour.parent = s
                    if neighbour in open:
                        open = removeItemFromPQ(open, neighbour)
                    heapq.heappush(open, ((neighbour.cost+sqrt((neighbour.position[0] - 0)**2 + (neighbour.position[1] - 19)**2)),neighbour))
    return None


s = AStar()
print("Path Costs: " + str(s.cost))
while not s == s.parent:
    s.symbol= "A"
    s = s.parent
s.symbol= "A"
printMap(field)