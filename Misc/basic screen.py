from graphics import *
import random

list1 = random.sample(range(1, 16), 15)

window_x, window_y = 900, 500
win = GraphWin("Window", window_x, window_y, autoflush=False)

def screenupdate():

    barSize = ((window_x) / len(list1))

    for rectPosition in range(len(list1)):

        rectx1 = rectPosition * barSize
        recty1 = 490
        rectx2 = rectPosition * barSize + barSize
        recty2 = (490 - 300 * list1[rectPosition] / len(list1)) - 5

        rect = Rectangle(Point(rectx1, recty1), Point(rectx2, recty2))
        rect.draw(win)


\
def main():

    screenupdate()


    win.getMouse()  # Pause to view result
    win.close()

main()
