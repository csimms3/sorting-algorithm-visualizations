import random
import time

def countingSort(list, exp1):
    n = len(list)

    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = list[i] // exp1
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = list[i] // exp1
        output[count[index % 10] - 1] = list[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, len(list)):
        list[i] = output[i]


def radixsort(list):


    start_time = time.time()

    max1 = max(list)
    exp = 1
    while max1 / exp > 0:
        countingSort(list, exp)
        exp *= 10

    time_taken = round(time.time() - start_time, 4)

    return time_taken

