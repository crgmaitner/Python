import graphics
from graphics import *
def main():
    win = GraphWin("A Target", 200, 200)
    center1 = Point(100, 100)
    shape1 = Circle(center1, 50)
    shape1.setFill('white')
    shape1.setOutline('black')
    shape1.draw(win)

    center2 = Point(100, 100)
    shape2 = Circle(center2, 40)
    shape2.setFill('black')
    shape2.setOutline('black')
    shape2.draw(win)

    center3 = Point(100, 100)
    shape3 = Circle(center3, 30)
    shape3.setFill('blue')
    shape3.setOutline('white')
    shape3.draw(win)

    center4 = Point(100, 100)
    shape4 = Circle(center4, 20)
    shape4.setFill('red')
    shape4.setOutline('white')
    shape4.draw(win)

    center5 = Point(100, 100)
    shape5 = Circle(center5, 10)
    shape5.setFill('yellow')
    shape5.setOutline('black')
    shape5.draw(win)
    win.getMouse()
    win.close()
main()