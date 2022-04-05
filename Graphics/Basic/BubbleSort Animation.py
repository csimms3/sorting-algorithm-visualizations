import random
from graphics import *

sample_size = int(input("Enter sample size : "))
sorting_speed = int(input("Enter sorting speed: "))
list1 = random.sample(range(0, sample_size), sample_size)  # (range(min, max), how many #)

window_x, window_y = 900, 500

win = GraphWin(f" Bubble Sort --- Sample size = {sample_size}, Sorting speed = {sorting_speed} swaps/second", window_x,
               window_y, autoflush=False)


def swap(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list[a], list[b]


def textcounter(iterations, swaps):

    counter = Text(Point(110, 20), f"Swaps = {swaps}  Iterations = {iterations}")
    counter.setTextColor(color_rgb(0, 0, 0))
    counter.setSize(15)
    counter.setFace('times roman')
    counter.draw(win)

    win.update()


def clearscreen(window):
    # print(window.find_all()) ---> debugging purposes

    for object in (window.find_all()):
        window.delete(object)


def screenupdate(num_list, iteration, swaps):

    barsize = ((window_x - window_x / 40) / len(num_list))

    clearscreen(win)

    for rectPosition in range(len(num_list)):

        rectx1 = window_x / 80 + (rectPosition * barsize)
        recty1 = window_y - window_y/40
        rectx2 = window_x / 80 + (rectPosition * barsize + barsize)
        recty2 = ((window_y - window_y/40) - 300 * (num_list[rectPosition] + 1) / len(num_list))

        rect = Rectangle(Point(rectx1, recty1), Point(rectx2, recty2))
        rect.draw(win)

    textcounter(iteration, swaps)

    update(sorting_speed)


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
                swap(list1, current_index - 1, current_index)

                iteration += 1
                actions_this_cycle += 1
                current_index += 1
                list_sorted = False

                # print(str(list1) + "Swaps : " + str(actions_this_cycle - 1), "Iteration : " + str(iteration) + " fwd")

                screenupdate(list, iteration, actions_this_cycle)

            else:
                iteration = iteration + 1
                current_index = current_index + 1

        while current_index > 1:
            if list[current_index] < list[current_index - 1]:
                swap(list1, current_index, current_index - 1)

                iteration += 1
                actions_this_cycle += 1
                current_index -= 1
                list_sorted = False

                # print(str(list) + "Swaps : " + str(actions_this_cycle - 1), "Iteration : " + str(iteration) + " bkwd")

                screenupdate(list, iteration, actions_this_cycle)

            else:
                iteration += 1
                current_index -= 1

        if list_sorted:
            actions_this_cycle = 0

            print("LIST SORTED")
            print(list)

    print("Iterations: " + str(iteration))
    print("%s seconds" % round(time.time() - start_time, 3))

sorting(list1)


win.getMouse()
win.close()
