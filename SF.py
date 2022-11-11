import sys
import math
import random

n = 1
eps = 1e-13
rand_max = 1024
dt = 0.993
OriginT = 20000


def distance(x):
    return math.fabs(x ** 2 - n)


def Simulated_Annealing():
    x = 0
    f = distance(x)
    T = OriginT
    while T > eps:
        dx = x + (random.randint(0, rand_max) * 2 - rand_max) * T
        while dx < 0:
            dx = x + (random.randint(0, rand_max) * 2 - rand_max) * T
        df = distance(dx)
        if df < f:
            x = dx
            f = df
        elif math.exp((f - df) / T) * rand_max > random.randint(0, rand_max):
            x = dx
            f = df

        T = T * dt
    return x


if __name__ == '__main__':
    n = int(input('your input number \n'))
    result = Simulated_Annealing()
    print('%.8f' % result)
