import random
import time

sample_size = int(input("Enter sample size : "))

list1 = random.sample(range(0, sample_size), sample_size)  # (range(min, max), how many #)

def swap(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list[a], list[b]

def sorting(list):

    start_time = time.time()

    print("STARTING CONFIGURATION :")
    print(list)

    listSorted = False

    while listSorted == False:

        listSorted = True

        for i in range(len(list) - 1):
            if list[i + 1] < list[i]:

                swap(list, i, i + 1)
                listSorted = False


    time_taken = round(time.time() - start_time, 3)
    print("%s seconds" % time_taken)
    print(list)

sorting(list1)