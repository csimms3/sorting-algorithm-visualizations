from graphics import *
import random

list1 = random.sample(range(1, 20), 19)
list2 = random.sample(range(1, 20), 19)

window_x, window_y = 900, 500
win = GraphWin("Window", window_x, window_y, autoflush=False)

def screenupdate(list):

    barSize = ((window_x) / len(list))

    for rectPosition in range(len(list)):

        rectx1 = rectPosition * barSize
        recty1 = 490
        rectx2 = rectPosition * barSize + barSize
        recty2 = (490 - 300 * list[rectPosition] / len(list))

        rect = Rectangle(Point(rectx1, recty1), Point(rectx2, recty2))
        rect.draw(win)

    update()



def main():

    screenupdate(list1)
    print(win.find_all())



    win.getMouse()  # Pause to view result
    win.close()

main()
