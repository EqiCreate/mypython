import math
import numpy as np
import copy


class Bee(object):
    def __init__(self, position, cost):
        self.Position = position
        self.Cost = cost

    def __repr__(self):
        return str(self.Cost) + '\t' + str(self.Position) + '\n'

    def __str__(self):
        return str(self.Cost)


def cost_function(x):
    return np.dot(x, x)


def roulette(p):
    r = np.random.rand()
    s = np.cumsum(p)
    y = next(x[0] for x in enumerate(s) if x[1] >= r)
    return y


if __name__ == '__main__':
    nVar = 5
    nVarSize = np.arange(nVar).reshape(1, nVar)
    varMin = -10
    varMax = 10
    nPop = 100
    nOnlooker = nPop
    maxIt = 400
    pop_index_array = np.arange(nPop)
    L = math.ceil(0.6 * nVar * nPop)
    empty_bee = Bee([], 0)
    pop = []
    BestCost = []
    BestSol = Bee(float('inf'), float('inf'))
    for i in range(0, nPop):
        entity = copy.copy(empty_bee)
        entity.Position = np.random.uniform(varMin, varMax, nVar)
        entity.Cost = cost_function(entity.Position)
        pop.append(entity)
        if entity.Cost <= BestSol.Cost:
            BestSol = entity
    print('%.8f' % BestSol.Cost)
    C = np.zeros(maxIt)
    for it in range(0, maxIt):
        for i in range(0, nPop):
            randomRange = np.delete(pop_index_array, i)
            k = np.random.choice(randomRange)
            phi = np.random.uniform(-1, 1, nVar)
            newPosition = pop[i].Position + np.dot(phi, pop[i].Position - pop[k].Position)
            newPosition[newPosition > varMax] = varMax
            newPosition[newPosition < varMin] = varMin
            newCost = cost_function(newPosition)
            if newCost <= pop[i].Cost:
                pop[i] = Bee(newPosition, newCost)
            else:
                C[i] += 1
        F = np.zeros(nPop)
        meanCost = sum([p.Cost for p in pop]) / len(pop)
        for i in range(0, nPop):
            F[i] = math.exp(-pop[i].Cost / meanCost)

        P = F / np.sum(F)

        for m in range(0, nOnlooker):
            i = roulette(P)
            randomRange = np.delete(pop_index_array, i)
            k = np.random.choice(randomRange)
            phi = np.random.uniform(-1, 1, nVar)
            newPosition = pop[i].Position + np.dot(phi, pop[i].Position - pop[k].Position)
            newPosition[newPosition > varMax] = varMax
            newPosition[newPosition < varMin] = varMin
            newCost = cost_function(newPosition)
            if newCost <= pop[i].Cost:
                pop[i] = Bee(newPosition, newCost)
            else:
                C[i] += 1
        # Detecting Bee
        for i in range(0, nPop):
            if C[i] >= L:
                xMax = np.max(pop[i].Position)
                xMin = np.min(pop[i].Position)
                pop[i].Position = np.random.uniform(xMin, xMax, nVar)
                pop[i].Cost = cost_function(pop[i].Position)
                C[i] = 0

        for i in range(0, nPop):
            if pop[i].Cost <= BestSol.Cost:
                BestSol = pop[i]

        BestCost.append(BestSol)

    print(BestCost)
