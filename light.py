import time
import graphics
from graphics import *

def main():
    print("This program will generate an image of a traffic signal based on user input.")
    print("Separate all input with a space.")
    
    a,b = input("Please provide a point to begin the signals rectangle: ").split()
    c,d = input("Provide a second point to complete the rectangle: ").split()
    
    e,f = input("Provide a point to center the first circle: ").split()
    print("You entered the point: ", (e, f))
    
    g,h = input("Provide a second point to center the second circle: ").split()
    print("You entered the point: ", (g, h))
    
    i,j = input("Provide a point to center the final circle: ").split()
    print("You entered the point: ", (i , j))
    
    print("Your traffic signal is now loading...")
    time.sleep(1)

    win = GraphWin('traffic_light',200,200)
    
    rect1 = Rectangle (Point(a, b), Point(c, d))
    rect1.setOutline("black")
    rect1.setWidth(2)
    rect1.setFill("black")
    rect1.draw(win)
    
    circ1 = Circle(Point(e, f), 20)
    circ1.setFill("red")
    circ1.setOutline ("black")
    circ1.setWidth(2)
    circ1.draw(win)

    circ2 = Circle(Point(g, h),20)
    circ2.setFill("yellow")
    circ2.setOutline ("black")
    circ2.setWidth(2)
    circ2.draw(win)

    circ3 = Circle (Point(i, j),20)
    circ3.setFill("green")
    circ3.setOutline ("black")
    circ3.setWidth(2)
    circ3.draw(win)
    
    win.getMouse()
    win.close()

main()