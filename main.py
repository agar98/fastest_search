import argparse
import random
import sys
import os

from utils.logs import Logger
from utils.arrayFunctions import generateArray, sortArray


def clear():
    return os.system('cls')


def get_args(args=None):
    parser = argparse.ArgumentParser(
        description="A tool to find out which is the fastest searching algorithm")

    parser.add_argument('-s', '--size', help="Size of array", default=100000)
    parser.add_argument(
        '-m', '--max', help="Biggest possible number", default=500000)
    parser.add_argument(
        '-d', '--details', help="Toggle for showing the details", choices=(True, False), default=True)

    results = parser.parse_args(args)

    return (
        results.size,
        results.max,
        results.details
    )


def main():
    arrSize, maxNum, showDetails = get_args(sys.argv[1:])
    clear()

    logger.printLog('info', 'Generating array')
    arr = generateArray(int(arrSize), int(maxNum))

    logger.printLog('info', 'Sorting array...')
    sortedArr = sortArray(arr)
    # clear()

    logger.printLog('success', 'Array sorted!')
    selectedIndex = random.randint(0, arrSize)
    logger.printLog('normal', f'Array size: {len(arr)}')
    logger.printLog(
        'normal', f'Selected Index: {selectedIndex}; Item at the position: {sortedArr[selectedIndex]}')


if __name__ == '__main__':
    logger = Logger()
    logger.banner()
    main()
