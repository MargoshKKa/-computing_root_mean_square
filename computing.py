import math


def get_square(number):
    return number*number


def get_sum(ints):
    sum = 0
    for item in ints:
        sum += get_square(item)
    return sum


def root_mean_square(ints):
    try:
        result = math.sqrt(get_sum(ints)/len(ints))
        return result
    except(ZeroDivisionError):
        print("There are no numbers to calculate")
        return 0
