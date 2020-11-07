from utils.performanceCalculator import performance
from utils.logs import print_log


@performance
def linear_search(target, array):
    search = [i for i in range(len(array)) if target == array[i]]
    print_log('success', f'Linear search found the target at {search[0]}')
