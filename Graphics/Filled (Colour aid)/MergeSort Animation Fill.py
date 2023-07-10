import random
import time
from graphics import *

iteration = 0
print("Ideal Inputs for \n Visualization: 100, 40 \n Explanation: 100, 40")
sample_size = int(input("Enter sample size (# > 0, # of data points to sort) : "))
update_rate = int(input("Enter update rate (Visual updates per second): "))
list1 = random.sample(range(0, sample_size), sample_size)  # (range(min, max), how many #)

window_x, window_y = 900, 500

win = GraphWin(f"Merge Sort --- Sample size = {sample_size}, Sorting speed = {update_rate} swaps/second",
               window_x, window_y, autoflush=False)

def wait(duration):
    if iteration == 0:
        for i in range(0,duration):
            print(f"Starting at {duration}: {i}")
            time.sleep(1)

def textcounter():
    global iteration
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


def screenupdate(list, i=-1, j=-1):
    barsize = ((window_x - window_x / 40) / len(list))

    clearscreen(win)

    for rectPosition in range(len(list)):

        if rectPosition == i or rectPosition == j:

            rectx1 = window_x / 80 + (rectPosition * barsize)
            recty1 = window_y - window_y / 40
            rectx2 = window_x / 80 + (rectPosition * barsize + barsize)
            recty2 = ((window_y - window_y / 40) - 300 * (list[rectPosition] + 1) / len(list))

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

    textcounter()

    update(update_rate)


def merge(list, w, a, b, low, y):
    i, j, k = a, low, a
    while i <= b and j <= y:
        if list[i] < list[j]:
            w[k], i = list[i], i + 1
        else:
            w[k], j = list[j], j + 1

        screenupdate(list, i, j)

        k += 1
    while i <= b:
        w[k], i, k = list[i], i + 1, k + 1
        screenupdate(list, i, j)

    while j <= y:
        w[k], j, k = list[j], j + 1, k + 1
        screenupdate(list, i, j)

    for i in range(a, y + 1):
        list[i] = w[i]
        screenupdate(list, i, j)


def mergesort(list, w, low, y):
    if low >= y:
        return
    m = (low + y) // 2
    mergesort(list, w, low, m)
    mergesort(list, w, m + 1, y)
    merge(list, w, low, m, m + 1, y)


def mergesortmain(list):
    start_time = time.time()

    print("STARTING CONFIGURATION :")
    print(list)

    mergesort(list, [0] * len(list), 0, len(list) - 1)

    print("LIST SORTED")
    print(list)

    print("Iterations: " + str(iteration))
    print("%s seconds" % round(time.time() - start_time, 3))


mergesortmain(list1)
