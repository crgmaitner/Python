#tlight2.py

from graphics import*

win = GraphWin()                                                    #Constructs the window in which the traffic light will be drawn.
button = Text(Point(120, 120), "Click here to quit.")               #Creates a line of text within the window displaying instructions.
button.draw(win)
def lbody(x, y, length, width, color, color2):                      #Defines a new function for the body of the traffic light.
    body = Rectangle (Point(x, y), Point(length, width))
    body.setOutline(color)
    body.setFill(color2)
    body.draw(win)

def light(color, color2, u, v, radius):                             #Defines a new function for each lamp of the traffic light.
    lightcolor = Circle(Point(u, v), radius)
    lightcolor.setOutline(color)
    lightcolor.setFill(color2)
    lightcolor.draw(win)

def main(x, y):                                                     #Begin main function here
    print("This program will generate an image of a traffic light using functions.")
    lbody (x, y, 40, 100, "black", "white")                         #Call the "lbody" function with appropriate arguments.
    light("black", "red", 20, 40, 9)                                #Call the "light" function with appropriate arguments.
    light("black", "yellow", 20, 60, 9)                             # " "
    light("black", "green", 20, 80, 9)                              # " "
    win.getMouse()
    print("Program terminated.")
main(2, 20)                                                         #Provides the position of the body of the traffic light.
