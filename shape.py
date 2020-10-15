import graphics
from graphics import *

def main():
	win = GraphWin()
	shape = Rectangle(Point(10, 5), Point(90, 195))
	shape.setOutline("black")
	shape.setFill("black")
	shape.draw(win)
	
	for i in range(10):
		p = win.getMouse()
		c = shape.getCenter()
		dx = p.getX() - c.getX()
		dy = p.getY() - c.getY()
		shape.move(dx, dy)
	win.close()
main()