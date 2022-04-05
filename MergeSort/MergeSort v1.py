import random
import time

sample_size = int(input("Enter sample size : "))

list1 = random.sample(range(0, sample_size), sample_size)  # (range(min, max), how many #)

def mergeSort(list):

    if len(list) > 1:

        mid = len(list)//2

        L = list[:mid]
        R = list[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1

            k += 1

        # Checking if any element is leftover (unsorted)
        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1

def mergeSortMain(list):

    start_time = time.time()
    iteration = 0

    print("STARTING CONFIGURATION :")
    print(list)

    mergeSort(list)

    print("LIST SORTED")
    print(list)

    print("Iterations: " + str(iteration))
    print("%s seconds" % round(time.time() - start_time, 3))

mergeSortMain(list1)
