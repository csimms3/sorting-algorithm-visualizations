import random
import time


def merge(list, outputlist, s1bb, s1tb, s2bb, s2tb):
    i, j, k = s1bb, s2bb, s1bb
    while i <= s1tb and j <= s2tb:
        if list[i] < list[j]:
            outputlist[k], i = list[i], i + 1
        else:
            outputlist[k], j = list[j], j + 1

        k += 1
    while i <= s1tb:
        outputlist[k], i, k = list[i], i + 1, k + 1

    while j <= s2tb:
        outputlist[k], j, k = list[j], j + 1, k + 1

    for i in range(s1bb, s2tb + 1):
        list[i] = outputlist[i]


def mergeSort(list, outputlist, low, high):
    if low >= high:
        return
    centre = (low + high) // 2
    mergeSort(list, outputlist, low, centre)
    mergeSort(list, outputlist, centre + 1, high)
    merge(list, outputlist, low, centre, centre + 1, high)


def mergeSortMain(list):

    start_time = time.time()

    mergeSort(list, [0] * len(list), 0, len(list) - 1)

    time_taken = round(time.time() - start_time, 4)

    return time_taken

