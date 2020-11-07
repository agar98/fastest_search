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


def clear():
    return os.system('cls')


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

    print_log('primary', 'Starting searches')
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print_log('primary', 'Finished!')


def show_results():
    table = PrettyTable()
    table.field_names = ['Algorithm', 'Time taken']

    for operation, time_taken in globalVariables.performance_list:
        algorithm = f"{operation}"
        time_taken_ms = f"{time_taken/1000000}ms"
        table.add_row([algorithm, time_taken_ms])

    print(table.get_string())


def main():
    arr_size, max_num = get_args(sys.argv[1:])

    generated_array = generate_array(int(arr_size), int(max_num))
    sorted_array = sort_array(generated_array)

    selected_index = random.randint(0, int(arr_size))
    selected_item = sorted_array[selected_index]
    print_log(
        'normal', f'Array size: {len(generated_array)}\nSelected Index: {selected_index}; Item at the position: {selected_item}')

    run_searches(selected_item, sorted_array)

    show_results()


if __name__ == '__main__':
    clear()
    globalVariables.init()
    banner()
    main()
