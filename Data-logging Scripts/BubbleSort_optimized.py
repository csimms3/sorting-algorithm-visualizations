import random
import time


def swap(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list[a], list[b]


def bubblesortoptimized(list):

    start_time = time.time()
    listSorted = False
    top = len(list) - 1

    while not listSorted:

        listSorted = True

        for i in range(0, top):
            if list[i + 1] < list[i]:

                swap(list, i, i + 1)
                listSorted = False

        top -= 1

    time_taken = round(time.time() - start_time, 4)

    return time_taken

