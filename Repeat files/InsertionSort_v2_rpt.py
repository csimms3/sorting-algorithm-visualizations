import random
import time

def swap(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list[a], list[b]

def insertionsort(list):
    iteration = 0

    start_time = time.time()

    for current_index in range(1, len(list)):

        key = list[current_index]

        j = current_index - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]

            iteration += 1
            j -= 1

        list[j + 1] = key #places element in correct spot (one after first smaller elementz)

    time_taken = round(time.time() - start_time, 4)

    return time_taken

