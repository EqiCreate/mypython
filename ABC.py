import math
import numpy as np
import copy


class Bee(object):
    def __int__(self, position, cost):
        self.Position = position
        self.Cost = cost

    def __repr__(self):
        return str(self.Cost) + '\t' + str(self.Position) + '\n'

    def __str__(self):
        return str(self.Cost)


def Z(x):
    return np.dot(x, x)


def roulette(p):
    r = np.random.rand()
    s = np.cumsum(p)
    y = next(x[0] for x in enumerate(s) if x[1] >= r)
    return y


if __name__ == '__main__':
    nVar = 5
    nVarSize = np.arange(nVar).reshape(1, nVar)
    varMin = 10
    pop = []
    BestCost = []
    BestSol = Bee(float('inf'), float('inf'))
