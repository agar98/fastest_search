import math
from utils.logs import print_log
from utils.performanceCalculator import performance


def jump_search_algorithm(target, array):
    length = len(array)

    step = math.sqrt(length)

    prev = 0
    while array[int(min(step, length)-1)] < target:
        prev = step
        step += math.sqrt(length)
        if prev >= length:
            return -1

    while array[int(prev)] < target:
        prev += 1

        if prev == min(step, length):
            return -1

    if array[int(prev)] == target:
        return prev

    return -1


@performance
def jump_search(target, array):
    index = jump_search_algorithm(target, array)

    if(index != -1):
        print_log(
            'success', f"Jump search found target at {math.trunc(index)}")
    else:
        print_log('error', 'Jump Search couldn\'t find target')
