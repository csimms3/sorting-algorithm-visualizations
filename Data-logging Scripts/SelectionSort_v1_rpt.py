import random
import time

def swap(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list[a], list[b]

def selectionsort(list):

    start_time = time.time()

    for i in range(len(list)):
        min = i

        for j in range(i + 1, len(list)):
            if list[min] > list[j]:
                min = j

        swap(list, min, i)

    time_taken = round(time.time() - start_time, 4)

    return time_taken
