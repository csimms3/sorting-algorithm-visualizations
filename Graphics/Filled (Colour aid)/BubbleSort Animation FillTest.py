import random
from graphics import *

iteration = 0

print("Ideal Inputs for \n Visualization: 50, 50 \n Explanation: 15, 2")
sample_size = int(input("Enter sample size (# > 0, # of data points to sort) : "))
update_rate = int(input("Enter update rate (Visual updates per second): "))
list1 = random.sample(range(0, sample_size), sample_size)  # (range(min, max), how many #)

window_x, window_y = 900, 500

win = GraphWin(f"Bubble Sort --- Sample size = {sample_size}, Sorting speed = {update_rate} swaps/second",
               window_x, window_y, autoflush=False)


def swap(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list[a], list[b]


def wait(duration):
    if iteration == 0:
        for i in range(0,duration):
            print(f"Starting at {duration}: {i}")
            time.sleep(1)


def textcounter():
    global iteration

    wait(10)

    iteration += 1
    counter = Text(Point(110, 20), f"Iterations = {iteration}")
    counter.setTextColor(color_rgb(0, 0, 0))
    counter.setSize(15)
    counter.setFace('times roman')
    counter.draw(win)

    win.update()


def clearscreen(window):
    # print(window.find_all()) ---> debugging purposes

    for object in (window.find_all()):
        window.delete(object)


def screenupdate(num_list, index):
    barsize = ((window_x - window_x / 40) / len(num_list))

    clearscreen(win)

    for rectPosition in range(len(num_list)):

        if rectPosition == index or rectPosition == index - 1:

            rectx1 = window_x / 80 + (rectPosition * barsize)
            recty1 = window_y - window_y / 40
            rectx2 = window_x / 80 + (rectPosition * barsize + barsize)
            recty2 = ((window_y - window_y / 40) - 300 * (num_list[rectPosition] + 1) / len(num_list))

            rect = Rectangle(Point(rectx1, recty1), Point(rectx2, recty2))
            rect.setFill("Green")
            rect.draw(win)

        else:

            rectx1 = window_x / 80 + (rectPosition * barsize)
            recty1 = window_y - window_y / 40
            rectx2 = window_x / 80 + (rectPosition * barsize + barsize)
            recty2 = ((window_y - window_y / 40) - 300 * (num_list[rectPosition] + 1) / len(num_list))

            rect = Rectangle(Point(rectx1, recty1), Point(rectx2, recty2))
            rect.setFill("White")
            rect.draw(win)

    textcounter()
    update(update_rate)


def sorting(list):
    current_index = 1  # current list index being checked
    actions_this_cycle = 1  # when 0 after full sweep === end

    start_time = time.time()

    print("STARTING CONFIGURATION :")
    print(list)

    while actions_this_cycle > 0:
        list_sorted = True  # checks to see if at least one swap occurred (not sorted)

        while current_index < len(list) - 1:
            if list[current_index - 1] > list[current_index]:
                swap(list1, current_index - 1, current_index)

                actions_this_cycle += 1
                current_index += 1
                list_sorted = False

                # print(str(list1) + "Swaps : " + str(actions_this_cycle - 1), "Iteration : " + str(iteration) + " fwd")

            else:
                current_index = current_index + 1

            screenupdate(list, current_index)

        while current_index > 1:
            if list[current_index] < list[current_index - 1]:
                swap(list1, current_index, current_index - 1)

                actions_this_cycle += 1
                current_index -= 1
                list_sorted = False

                # print(str(list) + "Swaps : " + str(actions_this_cycle - 1), "Iteration : " + str(iteration) + " bkwd")

            else:
                current_index -= 1

            screenupdate(list, current_index)

        if list_sorted:
            actions_this_cycle = 0

            print("LIST SORTED")
            print(list)

    print("%s seconds" % round(time.time() - start_time, 3))


sorting(list1)

win.getMouse()
win.close()
