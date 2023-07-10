import random
import time

sample_size = int(input("Enter sample size : "))

list1 = random.sample(range(0, sample_size), sample_size)  # (range(min, max), how many #)

def swap(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list[a], list[b]

def selectionsort(list):

    start_time = time.time()
    iteration = 0


    print("STARTING CONFIGURATION :")
    print(list)

    for i in range(len(list)):
        min = i

        for j in range(i + 1, len(list)):
            iteration += 1
            if list[min] > list[j]:
                min = j

        swap(list, min, i)

    print("LIST SORTED")
    print(list)

    print("Iterations: " + str(iteration))
    print("%s seconds" % round(time.time() - start_time, 3))

selectionsort(list1)