import math


def root_mean_square(values):
    return math.sqrt(sum(x**2 for x in values)/len(values))