import graphics
from graphics import *

def main():
    win = GraphWin()
    leftEye = Rectangle(Point(10, 10), Point(60, 60))
    leftEye.setOutline("blue")
    leftEye.setFill("black")
    leftEye.draw(win)
    rightEye = leftEye.clone()
    rightEye.draw(win)
    
    for i in range(10):
        p = win.getMouse()
        c = rightEye.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        rightEye.move(dx, dy)
    win.close()
main()