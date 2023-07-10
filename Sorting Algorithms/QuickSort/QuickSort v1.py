import random
import time

sample_size = int(input("Enter sample size : "))
list1 = random.sample(range(0, sample_size), sample_size)  # (range(min, max), how many #)




def partition(list, low, high):
    index = (low - 1)
    pivot = list[high]
    for j in range(low, high):
        if list[j] <= pivot:
            index += 1
            list[index], list[j] = list[j], list[index]
    list[index + 1], list[high] = list[high], list[index + 1]
    return (index + 1)

def quickSort(list, low, high):
    if len(list) == 1:
        return list
    if low < high:
        cut = partition(list, low, high)
        quickSort(list, low, cut - 1)
        quickSort(list, cut + 1, high)

def quickSortMain(list, low, high):

    start_time = time.time()
    print(f"STARTING CONFIGURATION : {list1}")

    quickSort(list, low, high)

    time_taken = round(time.time() - start_time, 3)
    print("LIST SORTED")
    print(list)
    print("%s seconds" % time_taken)


quickSortMain(list1, 0, (len(list1) - 1))