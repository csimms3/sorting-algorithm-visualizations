import random
from graphics import *

iteration = 0

print("Ideal Inputs for \n Visualization: 50, 20 \n Explanation: 15, 2")
sample_size = int(input("Enter sample size (# > 0, # of data points to sort) : "))
update_rate = int(input("Enter update rate (Visual updates per second): "))
list1 = random.sample(range(0, sample_size), sample_size)  # (range(min, max), how many #)

window_x, window_y = 900, 500

win = GraphWin(f"Insertion Sort --- Sample size = {sample_size}, Sorting speed = {update_rate} swaps/second",
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


def screenupdate(num_list, current_index, index):
    barsize = ((window_x - window_x / 40) / len(num_list))

    clearscreen(win)

    for rectPosition in range(len(num_list)):

        if current_index >= rectPosition >= index:

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


def insertionsort(list):
    start_time = time.time()

    print("STARTING CONFIGURATION :")
    print(list)

    for current_index in range(1, len(list)):

        key = list[current_index]
        j = current_index - 1

        while j >= 0 and key < list[j]:
            list[j + 1], list[j] = list[j], list[j+1]

            screenupdate(list, current_index, j)

            j -= 1

        screenupdate(list, current_index, j)

    print("LIST SORTED")
    print(list)

    print("%s seconds" % round(time.time() - start_time, 3))


insertionsort(list1)

win.getMouse()
win.close()
