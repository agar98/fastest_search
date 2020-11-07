import random
from utils.logs import print_log
from utils.performanceCalculator import performance


@performance
def generate_array(size, max_number):
    print_log('info', 'Generating array')

    arr = random.sample(range(1, max_number), size)
    return arr


def quick_sort(array):
    if array == []:
        return []
    else:
        pivot = array[0]
        lesser = quick_sort([x for x in array[1:] if x < pivot])
        greater = quick_sort([x for x in array[1:] if x >= pivot])
        return lesser + [pivot] + greater


@performance
def sort_array(array):
    print_log('info', 'Sorting array...')

    arr = quick_sort(array)

    print_log('success', 'Array sorted!')

    return arr
