import random
import time

sample_size = int(input("Enter sample size : "))

list1 = random.sample(range(0, sample_size), sample_size)  # (range(min, max), how many #)


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr[a], arr[b]


def bubblesortoptimized(arr):
    start_time = time.time()
    list_sorted = False
    top = len(list1) - 1
    while not list_sorted:
        list_sorted = True
        for i in range(0, top):
            if arr[i + 1] < arr[i]:
                swap(arr, i, i + 1)
                list_sorted = False
        top -= 1
    time_taken = round(time.time() - start_time, 4)
    return time_taken

