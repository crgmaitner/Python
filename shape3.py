import graphics
from graphics import *

def main():
    win = GraphWin("Click and Type", 400, 400)
    shape = Rectangle(Point(10, 10), Point(80, 80))
    shape.setOutline("black")
    shape.setFill("black")
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)
    button = Text(Point(150, 150), "Click again to quit.")
    button.draw(win)
    win.getMouse()
    Rectangle(Point(100, 110), Point(120, 145).draw(win))
    win.close()
main()