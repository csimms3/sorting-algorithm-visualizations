import random
import time

sample_size = int(input("Enter sample size : "))

list1 = random.sample(range(0, sample_size), sample_size)  # (range(min, max), how many #)

def swap(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list[a], list[b]

def insertionsort(list):

    start_time = time.time()
    iteration = 0

    print("STARTING CONFIGURATION :")
    print(list)

    for current_index in range(1, len(list)):

        key = list[current_index]

        j = current_index - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]

            iteration += 1
            j -= 1

        list[j + 1] = key #places element in correct spot (one after first smaller elementz)

    print("LIST SORTED")
    print(list)

    print("Iterations: " + str(iteration))
    print("%s seconds" % round(time.time() - start_time, 3))

insertionsort(list1)