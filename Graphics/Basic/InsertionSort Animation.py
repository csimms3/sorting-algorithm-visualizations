import random
from graphics import *

'''fix this'''

sample_size = int(input("Enter sample size : "))
sorting_speed = int(input("Enter sorting speed: "))
list1 = random.sample(range(0, sample_size), sample_size)  # (range(min, max), how many #)

window_x, window_y = 900, 500

win = GraphWin(f" Insertion Sort --- Sample size = {sample_size}, Sorting speed = {sorting_speed} swaps/second", window_x,
               window_y, autoflush=False)


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


def screenupdate(num_list, iteration):

    barsize = ((window_x - window_x / 40) / len(num_list))

    clearscreen(win)

    for rectPosition in range(len(num_list)):

        rectx1 = window_x / 80 + (rectPosition * barsize)
        recty1 = window_y - window_y/40
        rectx2 = window_x / 80 + (rectPosition * barsize + barsize)
        recty2 = ((window_y - window_y/40) - 300 * (num_list[rectPosition] + 1) / len(num_list))

        rect = Rectangle(Point(rectx1, recty1), Point(rectx2, recty2))
        rect.draw(win)

    textcounter(iteration)

    update(sorting_speed)


def insertionsort(list):

    start_time = time.time()
    iteration = 0


    print("STARTING CONFIGURATION :")
    print(list)

    for current_index in range(1, len(list)):

        key = list[current_index]

        j = current_index - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]

            iteration += 1
            j -= 1

        list[j + 1] = key
        screenupdate(list, iteration)

    print("LIST SORTED")
    print(list)

    print("Iterations: " + str(iteration))
    print("%s seconds" % round(time.time() - start_time, 3))


insertionsort(list1)


win.getMouse()
win.close()
