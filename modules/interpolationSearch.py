from utils.logs import print_log
from utils.performanceCalculator import performance


def interpolation_search_algorithm(arr, n, x):
    lo = 0
    hi = (n - 1)

    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        if lo == hi:
            if arr[lo] == x:
                return lo
            return -1

        pos = lo + int(((float(hi - lo) /
                         (arr[hi] - arr[lo])) * (x - arr[lo])))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            lo = pos + 1

        else:
            hi = pos - 1

    return -1


@performance
def interpolation_search(target, array):
    index = interpolation_search_algorithm(array, len(array), target)

    if(index != -1):
        print_log(
            'success', f"Interpolation search found the target at {index}")
    else:
        print_log('error', 'Interpolation Search couldn\'t find target')
