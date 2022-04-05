import random
import time

sample_size = int(input("Enter sample size : "))

list1 = random.sample(range(0, sample_size), sample_size)  # (range(min, max), how many #)

def heapify(list, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and list[largest] < list[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and list[largest] < list[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        list[i], list[largest] = list[largest], list[i]  # swap

        # Heapify the root.
        heapify(list, n, largest)


def heapSort(list):
    n = len(list)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(list, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]  # swap
        heapify(list, i, 0)

    print("LIST SORTED")
    print(list)

heapSort(list1)