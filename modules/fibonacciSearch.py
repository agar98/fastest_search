from utils.performanceCalculator import performance
from utils.logs import print_log


def fibonacci_search_algorithm(arr, x, n):
    fibMMm2 = 0  # (m-2)'th Fibonacci No.
    fibMMm1 = 1  # (m-1)'th Fibonacci No.
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci

    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    offset = -1

    while (fibM > 1):

        i = min(offset+fibMMm2, n-1)

        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i

        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1

        else:
            return i

    if(fibMMm1 and arr[offset+1] == x):
        return offset+1

    return -1


@performance
def fibonacci_search(target, array):
    index = fibonacci_search_algorithm(array, target, len(array))

    if(index != -1):
        print_log('success', f"Fibonacci Search found the target at {index}")
    else:
        print_log('error', 'Fibonacci Search couldn\'t find target')
