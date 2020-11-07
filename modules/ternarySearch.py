from utils.performanceCalculator import performance
from utils.logs import print_log


@performance
def ternary_search(target, array):
    left = 0
    right = len(array) - 1
    index = -1

    while left <= right:
        ind1 = left
        ind2 = left + (right - left) // 3
        ind3 = left + 2 * (right - left) // 3
        if target == array[left]:
            print_log('success', f'Ternary Search found the target at {left}')
            return
        elif target == array[right]:
            print_log('success', f'Ternary Search found the target at {right}')
            return
        elif target < array[left] or target > array[right]:
            print_log('error', "Teranry search was not able to find target")
            return
        elif target <= array[ind2]:
            right = ind2
        elif target > array[ind2] and target <= array[ind3]:
            left = ind2 + 1
            right = ind3
        else:
            left = ind3 + 1
