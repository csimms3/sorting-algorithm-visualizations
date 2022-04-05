import random
import time

sample_size = int(input("Enter sample size : "))

list1 = random.sample(range(0, sample_size), sample_size)  # (range(min, max), how many #)

''' for the love of god fix this and rename stuff'''

def merge(list, w, a, b, low, y):
    i, j, k = a, low, a
    while i <= b and j <= y:
        if list[i] < list[j]:
            w[k], i = list[i], i + 1
        else:
            w[k], j = list[j], j + 1

        k += 1
    while i <= b:
        w[k], i, k = list[i], i + 1, k + 1

    while j <= y:
        w[k], j, k = list[j], j + 1, k + 1

    for i in range(a, y + 1):
        list[i] = w[i]


def mergeSort(list, w, low, y):
    if low >= y:
        return
    m = (low + y) // 2
    mergeSort(list, w, low, m)
    mergeSort(list, w, m + 1, y)
    merge(list, w, low, m, m + 1, y)

def mergeSortMain(list):

    start_time = time.time()
    iteration = 0

    print("STARTING CONFIGURATION :")
    print(list)

    mergeSort(list, [0] * len(list), 0, len(list) - 1)

    print("LIST SORTED")
    print(list)

    print("Iterations: " + str(iteration))
    print("%s seconds" % round(time.time() - start_time, 3))

mergeSortMain(list1)
