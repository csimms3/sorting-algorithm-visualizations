import random
import time

sample_size = int(input("Enter sample size : "))

list1 = random.sample(range(0, sample_size), sample_size)  # (range(min, max), how many #)

def swap(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list[a], list[b]

def insertionsort(list):
    for current_index in range(1, len(list)):
        key = list[current_index]
        j = current_index - 1
        while j >= 0 and key < list[j]:
            swap(list, j, j+1)
            j -= 1
    print(list)

insertionsort(list1)