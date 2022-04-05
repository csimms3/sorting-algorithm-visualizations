import random
import time
from graphics import *

sample_size = int(input("Enter sample size : "))
sorting_speed = int(input("Enter sorting speed: "))
list1 = random.sample(range(0, sample_size), sample_size)  # (range(min, max), how many #)

window_x, window_y = 900, 500

win = GraphWin(f" Insertion Sort --- Sample size = {sample_size}, Sorting speed = {sorting_speed} swaps/second",
               window_x, window_y, autoflush=False)

''' fix colour bar, not clear'''


def textcounter(iterations):

    counter = Text(Point(70, 20), f"Iterations = {iterations}")
    counter.setTextColor(color_rgb(0, 0, 0))
    counter.setSize(15)
    counter.setFace('times roman')
    counter.draw(win)

    win.update()


def clearscreen(window):
    # print(window.find_all()) ---> debugging purposes

    for object in (window.find_all()):
        window.delete(object)


def screenupdate(list, index, iteration):

    barsize = ((window_x - window_x / 40) / len(list))

    clearscreen(win)

    for rectPosition in range(len(list)):

        if rectPosition == index:

            rectx1 = window_x / 80 + (rectPosition * barsize)
            recty1 = window_y - window_y/40
            rectx2 = window_x / 80 + (rectPosition * barsize + barsize)
            recty2 = ((window_y - window_y/40) - 300 * (list[rectPosition] + 1) / len(list))

            rect = Rectangle(Point(rectx1, recty1), Point(rectx2, recty2))
            rect.setFill("Green")
            rect.draw(win)


        else:
            rectx1 = window_x / 80 + (rectPosition * barsize)
            recty1 = window_y - window_y / 40
            rectx2 = window_x / 80 + (rectPosition * barsize + barsize)
            recty2 = ((window_y - window_y / 40) - 300 * (list[rectPosition] + 1) / len(list))

            rect = Rectangle(Point(rectx1, recty1), Point(rectx2, recty2))
            rect.setFill("White")
            rect.draw(win)

    textcounter(iteration)

    update(sorting_speed)


def swap(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list[a], list[b]


def partition(list, low, high):
    i = low - 1
    pivot = list[high]

    for j in range(low, high):

        if list[j] <= pivot:

            i = i + 1
            swap(list, i, j)

            screenupdate(list, i, 0)

    swap(list, i + 1, high)
    return (i + 1)


def quickSort(list, low, high):

    if len(list) == 1:
        return list
    if low < high: # essentially a while = true statement

        cut = partition(list, low, high)

        quickSort(list, low, cut - 1)
        quickSort(list, cut + 1, high)


def quickSortMain(list, low, high):

    start_time = time.time()
    print(f"STARTING CONFIGURATION : {list1}")

    quickSort(list, low, high)

    screenupdate(list, len(list) - 1, 0)

    print("LIST SORTED")
    print(list)
    print("%s seconds" % round(time.time() - start_time, 3))

    win.getMouse()
    win.close()


quickSortMain(list1, 0, (len(list1) - 1))


