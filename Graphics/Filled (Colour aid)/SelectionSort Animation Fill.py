import random
from graphics import *

iteration = 0

print("Ideal Inputs for \n Visualization: 40, 50 \n Explanation: 15, 2")
sample_size = int(input("Enter sample size (# > 0, # of data points to sort) : "))
update_rate = int(input("Enter update rate (Visual updates per second): "))
list1 = random.sample(range(0, sample_size), sample_size)  # (range(min, max), how many #)

window_x, window_y = 900, 500

win = GraphWin(f"Selection Sort --- Sample size = {sample_size}, Sorting speed = {update_rate} swaps/second",
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
    counter = Text(Point(70, 20), f"Iterations = {iteration}")
    counter.setTextColor(color_rgb(0, 0, 0))
    counter.setSize(15)
    counter.setFace('times roman')
    counter.draw(win)

    win.update()


def clearscreen(window):
    # print(window.find_all()) ---> debugging purposes

    for object in (window.find_all()):
        window.delete(object)


def screenupdate(num_list, j, min):

    barsize = ((window_x - window_x / 40) / len(num_list))

    clearscreen(win)

    for rectPosition in range(len(num_list)):

        if rectPosition == j or rectPosition == min:

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


def selectionsort(list):

    start_time = time.time()


    print("STARTING CONFIGURATION :")
    print(list)

    for i in range(len(list)):
        min = i

        for j in range(i + 1, len(list)):
            screenupdate(list, j, min)

            if list[min] > list[j]:
                min = j

        screenupdate(list, j, min)

        swap(list, min, i)

    print("LIST SORTED")
    print(list)

    print("%s seconds" % round(time.time() - start_time, 3))

selectionsort(list1)


win.getMouse()
win.close()
