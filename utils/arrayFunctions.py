import random


def generateArray(size, maxNumber):
    arr = random.sample(range(1, maxNumber), size)
    return arr


def sortArray(array):
    if array == []:
        return []
    else:
        pivot = array[0]
        lesser = sortArray([x for x in array[1:] if x < pivot])
        greater = sortArray([x for x in array[1:] if x >= pivot])
        return lesser + [pivot] + greater
