import random
import time


def swap(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list[a], list[b]


def bubblesortfast(list):
    current_index = 1  # current list index being checked
    actions_this_cycle = 1  # when 0 after full sweep === end

    start_time = time.time()

    while actions_this_cycle > 0:
        list_sorted = True  # checks to see if at least one swap occurred (not sorted)

        while current_index < len(list) - 1:
            if list[current_index - 1] > list[current_index]:
                swap(list, current_index - 1, current_index)

                actions_this_cycle += 1
                list_sorted = False

            current_index = current_index + 1

        while current_index > 1:
            if list[current_index] < list[current_index - 1]:
                swap(list, current_index, current_index - 1)

                actions_this_cycle += 1
                list_sorted = False

            current_index -= 1

        if list_sorted:
            actions_this_cycle = 0

    time_taken = round(time.time() - start_time, 4)

    return time_taken


