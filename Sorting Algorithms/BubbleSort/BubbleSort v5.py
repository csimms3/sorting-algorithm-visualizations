# Improved Algorithm, sorts forward once fully, then runs backwards (as in v2)




"""fix else statements in this and anim, put var updates out of if statement -- simplify"""

import random
import time

sample_size = 1000
#int(input("Enter sample size : "))

# list = random.sample(range(0, sample_size), sample_size)  # (range(min, max), how many #)

def swap(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list[a], list[b]


def sorting(list):

    current_index = 1  # current list index being checked
    actions_this_cycle = 1  # when 0 after full sweep === end
    iteration = 0

    start_time = time.time()

    print("STARTING CONFIGURATION :")
    print(list)


    while actions_this_cycle > 0:
        list_sorted = True  # checks to see if at least one swap occurred (not sorted)

        while current_index < len(list) - 1:
            if list[current_index - 1] > list[current_index]:
                swap(list, current_index - 1, current_index)

                iteration += 1
                actions_this_cycle += 1
                current_index += 1
                list_sorted = False

                # print(str(list1) + "Swaps : " + str(actions_this_cycle - 1), "Iteration : " + str(iteration) + " fwd")

            else:
                iteration = iteration + 1
                current_index = current_index + 1

        while current_index > 1:
            if list[current_index] < list[current_index - 1]:
                swap(list, current_index, current_index - 1)

                iteration += 1
                actions_this_cycle += 1
                current_index -= 1
                list_sorted = False

                # print(str(list1) + "Swaps : " + str(actions_this_cycle - 1), "Iteration : " + str(iteration) + " bkwd")

            else:
                iteration = iteration + 1
                current_index = current_index - 1

        if list_sorted:
            actions_this_cycle = 0

    time_taken = round(time.time() - start_time, 3)

    print("LIST SORTED")
    print(list)
    print("Iterations: " + str(iteration))
    print("%s seconds" % time_taken)

    return time_taken


def repeat(reps, sample_size):

    timearr = []

    for i in range(0, reps):
        list1 = random.sample(range(0, sample_size), sample_size)

        timearr.append(sorting(list1))

        list1 = []


    print(timearr)

repeat(20, 1000)