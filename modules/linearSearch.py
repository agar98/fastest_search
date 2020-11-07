from utils.performanceCalculator import performance
from utils.logs import print_log


@performance
def linear_search(target, array):
    print_log('info', '\nStarting Linear Search')
    search = [i for i in range(len(array)) if target == array[i]]
    print_log('success', f'Found at {search[0]}!')
