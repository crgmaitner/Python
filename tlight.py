import time
import graphics
from graphics import *

def main():
    print("This program will generate a graphic image of a traffic signal.")
    enter = input("Press enter to load the image.")
	
    print("Your traffic signal is now loading...")
    time.sleep(1)
	
    win = GraphWin('traffic_light', 200, 200)
    
    rect1 = Rectangle (Point(50, 30), Point(110, 170))
    rect1.setOutline("black")
    rect1.setWidth(2)
    rect1.setFill("white")              #Was black, changed to white.
    rect1.draw(win)
    
    circ1 = Circle(Point(80, 55), 20)
    circ1.setFill("red")
    circ1.setOutline ("black")
    circ1.setWidth(2)
    circ1.draw(win)

    circ2 = Circle(Point(80, 100),20)
    circ2.setFill("yellow")
    circ2.setOutline ("black")
    circ2.setWidth(2)
    circ2.draw(win)

    circ3 = Circle (Point(80, 145),20)
    circ3.setFill("green")
    circ3.setOutline ("black")
    circ3.setWidth(2)
    circ3.draw(win)
    
    win.getMouse()
    win.close()
    
    print("Goodbye.")
main()