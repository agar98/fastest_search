import argparse
import random
import sys
import time
import os
from threading import Thread
from prettytable import PrettyTable

import utils.globalVariables as globalVariables
from utils.logs import print_log, banner
from utils.arrayFunctions import generate_array, sort_array

from modules.linearSearch import linear_search
from modules.binarySearch import binary_search
from modules.jumpSearch import jump_search
from modules.interpolationSearch import interpolation_search
from modules.fibonacciSearch import fibonacci_search
from modules.exponentialSearch import exponential_search
from modules.ternarySearch import ternary_search


def clear():
    return os.system('cls')


def findFromPerformance():
    fastest = 1000000000000000000000
    fastest_name = ""
    slowest = 0
    slowest_name = ""

    for operation, time_taken in globalVariables.performance_list:
        if(operation == 'generate_array' or operation == 'sort_array'):
            continue

        if(fastest > time_taken):
            fastest = time_taken
            fastest_name = operation

        if(slowest < time_taken):
            slowest = time_taken
            slowest_name = operation

    return (
        fastest,
        fastest_name,
        slowest,
        slowest_name
    )


def get_args(args=None):
    parser = argparse.ArgumentParser(
        description="A tool to find out which is the fastest searching algorithm")

    parser.add_argument('-s', '--size', help="Size of array", default=100000)
    parser.add_argument(
        '-m', '--max', help="Biggest possible number", default=500000)

    results = parser.parse_args(args)

    return (
        results.size,
        results.max
    )


def run_searches(target, array):
    t1 = Thread(target=linear_search, args=(target, array))
    t2 = Thread(target=binary_search, args=(target, array))
    t3 = Thread(target=jump_search, args=(target, array))
    t4 = Thread(target=interpolation_search, args=(target, array))
    t5 = Thread(target=exponential_search, args=(target, array))
    t6 = Thread(target=fibonacci_search, args=(target, array))
    t7 = Thread(target=ternary_search, args=(target, array))

    print_log('heading', '\n\n----- Starting searches -----')
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    print_log('info', 'Finished!')


def show_results():
    table = PrettyTable()
    table.field_names = ['Algorithm', 'Time taken']

    for operation, time_taken in globalVariables.performance_list:
        if(operation == 'generate_array' or operation == 'sort_array'):
            continue

        algorithm = f"{operation}"
        time_taken_ms = f"{time_taken/1000000}ms"
        table.add_row([algorithm, time_taken_ms])

    fastest, f_name, slowest, s_name = findFromPerformance()

    print_log('heading', '\n\n----- Results -----')

    print(table.get_string())

    print_log(
        'primary', f'\nFastest search: {f_name} - {fastest/1000000}ms\nSlowest search: {s_name} - {slowest/1000000}ms')


def main():
    arr_size, max_num = get_args(sys.argv[1:])

    if(int(arr_size) > int(max_num)):
        print_log(
            'error', 'Size of the array cannot be bigger than the range of numbers')
        sys.exit(1)

    generated_array = generate_array(int(arr_size), int(max_num))
    sorted_array = sort_array(generated_array)

    selected_index = random.randint(0, int(arr_size))
    selected_item = sorted_array[selected_index]
    print_log(
        'normal', f'\nArray size: {len(generated_array)}\nSelected Index: {selected_index}\nItem at the position: {selected_item}')

    run_searches(selected_item, sorted_array)

    show_results()


if __name__ == '__main__':
    clear()
    globalVariables.init()
    banner()
    main()
