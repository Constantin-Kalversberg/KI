from src.P2.board import *
from random import randint

def createRandomPopulation(size):
    population = []
    for i in range(size):
        string = ""
        for i in range(8):
            string = string + str(randint(1,8))
        population.append(Board(string))
    return population

def Reproduce(x, y):
    n = randint(1, len(x.queenPos)-1)
    return Board(x.queenPos[0 : n] + y.queenPos[-(len(x.queenPos) -n):])
    #return (x.queenPos[0 : n] + y.queenPos[-(len(x.queenPos) -n):], y.queenPos[0 : n] + x.queenPos[-(len(x.queenPos) -n):])

def fitness(individual):
    return 28 - individual.heuristics()

def RandomSelection(population, fitnessFunction):
    population.sort(key = lambda x : fitnessFunction(x), reverse=True)
    return population[randint(0,len(population)*0.5)]

def GeneticAlgorithm(population, fitnessFunction):
    for i in range(100):
        newPopulation = []
        population.sort(key = lambda x : fitnessFunction(x), reverse=True)
        print("Iteration: " + str(i))
        population[0].printBoard()
        if (population[0].heuristics() == 0):
            break
        for j in range(len(population)):
            x = RandomSelection(population, fitnessFunction)
            y = RandomSelection(population, fitnessFunction)
            child = Reproduce(x,y)
            if(randint(0,100)<10):
                child.move(randint(0,8), randint(0,8))
            newPopulation.append(child)
        population = newPopulation

    population.sort(key = lambda x : fitnessFunction(x), reverse=True)
    return population[0]

GeneticAlgorithm(createRandomPopulation(50), fitness)

#--------------Task 2.3------------------

