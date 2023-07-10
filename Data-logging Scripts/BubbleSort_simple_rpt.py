import random
import time


def swap(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list[a], list[b]


def bubblesortsimple(list):

    start_time = time.time()

    listSorted = False

    while listSorted == False:

        listSorted = True

        for i in range(len(list) - 1):
            if list[i + 1] < list[i]:
                swap(list, i, i + 1)
                listSorted = False

    time_taken = round(time.time() - start_time, 4)

    return time_taken




