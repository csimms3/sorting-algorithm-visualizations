import random
import time

def swap(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list[a], list[b]


def partition(list, low, high):
    index = (low - 1)
    pivot = list[high]

    for j in range(low, high):

        if list[j] <= pivot:

            index += 1
            swap(list, index, j)

    swap(list, index + 1, high)
    return (index + 1)


def quickSort(list, low, high):

    if len(list) == 1:
        return list
    if low < high:

        cut = partition(list, low, high)

        quickSort(list, low, cut - 1)
        quickSort(list, cut + 1, high)


def quickSortMain(list):

    start_time = time.time()

    quickSort(list, 0, len(list)-1)

    time_taken = round(time.time() - start_time, 4)

    return time_taken



