import random
import time

sample_size = int(input("Enter sample size : "))

list1 = random.sample(range(0, sample_size), sample_size)  # (range(min, max), how many #)

def bubblesortoptimized(arr):
    print(arr)
    list_sorted = False
    top = len(list1) - 1
    while not list_sorted:
        list_sorted = True
        for i in range(0, top):
            if arr[i + 1] < arr[i]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                list_sorted = False
        top -= 1
    print(arr)

bubblesortoptimized(list1)