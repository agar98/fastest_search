from utils.performanceCalculator import performance
from utils.logs import print_log


def binary_search_algorithm(array, l, r, target):
    if r >= l:
        mid = l + (r - l) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binary_search_algorithm(array, l, mid-1, target)
        else:
            return binary_search_algorithm(array, mid + 1, r, target)

    else:
        return -1


@performance
def binary_search(target, array):
    # print_log('info', '\nStarting Binary Search')

    index = binary_search_algorithm(array, 0, len(array) - 1, target)

    if(index != -1):
        print_log('success', f'Binary Search found the target at {index}')
    else:
        print_log('error', 'Binary Search couldn\'t find target')
