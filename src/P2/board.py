import types
from abc import abstractmethod
import math
from random import randint

class Board:
    def __init__(self, queenPos = "00000000", transition = None):
        self.queenPos = queenPos
        if not transition == None:
            self.transitionModel = types.MethodType(transition, self)

    def heuristics(self):
        collisions = 0
        for i in range(8):
            interested_queen = int(self.queenPos[i])
            if interested_queen >= 1 and interested_queen <=8:
                for j in range(i+1, 8):
                    other_queen = int(self.queenPos[j])
                    if other_queen != 0:
                        if interested_queen == other_queen or \
                                                interested_queen - (j-i) == other_queen or \
                                                interested_queen + (j-i) == other_queen:
                            collisions += 1
        return collisions

    def printBoard(self):
        for i in range(1,9):
            row = ""
            for j in range(8):
                if(int(self.queenPos[j]) == i):
                    row += "o"
                else:
                    row += "*"

            print(row)
        print(self.queenPos)
        print("h() = "  + str(self.heuristics()))
        print()

    def move(self, queen, pos):
        s = list(self.queenPos)
        s[queen-1] = str(pos)
        self.queenPos = ''.join(s)

    @abstractmethod
    def transitionModel(self):
        pass
