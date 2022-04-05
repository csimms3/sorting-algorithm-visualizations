from graphics import *

list1 = [3, 2, 1]
list2 = []
win = GraphWin("Window", 500, 500)

class Rect:

    def __init__(self, index): ## height is index value, ex. index = 1, height = list[index] (list[1])
        self.height = list1[index]
        self.index = index

    def draw_rect(self):
        self.rect = Rectangle(Point(), Point())  # use index and height to draw correctly

    def update_rect(self, index):
        self.height = list1[index]

r1 = Rect(0)

list2.append(r1.height)

print(list2)





