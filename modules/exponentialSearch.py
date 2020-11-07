from utils.performanceCalculator import performance
from utils.logs import print_log


def binary_search(array, l, r, target):
    if r >= l:
        mid = int(l + (r - l) // 2)

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binary_search(array, l, mid-1, target)
        else:
            return binary_search(array, mid + 1, r, target)

    else:
        return -1


def exponential_search_algorithm(arr, n, x):
    if arr[0] == x:
        return 0

    i = 1
    while i < n and arr[i] <= x:
        i = i * 2

    return binary_search(arr, i / 2, min(i, n-1), x)


@performance
def exponential_search(target, array):
    index = exponential_search_algorithm(array, len(array), target)

    if(index != -1):
        print_log('success', f'Exponential Search found the target at {index}')
    else:
        print_log('error', 'Exponential Search couldn\'t find target')
