#target.py

import graphics
from graphics import *
import math
import time

def shot(point1, circle):                                               #Defines a new function called "shot".

    x = point1.getX() - circle.getCenter().getX()
    y = point1.getY() - circle.getCenter().getY()
    dist = math.sqrt(x * x + y * y)
    
    return dist <= circle.getRadius()

def main():                                                             #Begin main function here.
    print("This program allows the user to play a simple archery game.")
    print("Get ready!")
    time.sleep(1)
    print("Go!")
    score = 0

    win = GraphWin()
    shape1 = Circle(Point(100,100), 10)
    shape1.setFill("yellow")
    shape1.setOutline("yellow")
    
    shape2 = Circle(Point(100,100), 20)
    shape2.setFill("red")
    shape2.setOutline("red")
    
    shape3 = Circle(Point(100,100), 30)
    shape3.setFill("blue")
    shape3.setOutline("blue")
    
    shape4 = Circle(Point(100,100), 40)
    shape4.setFill("black")
    shape4.setOutline("black")
    
    shape5 = Circle(Point(100,100), 50)
    shape5.setFill("white")
    shape5.setOutline("black")
    
    shape5.draw(win)
    shape4.draw(win)
    shape3.draw(win)
    shape2.draw(win)
    shape1.draw(win)
 
    for i in range(5):                                                  #Creates a loop to allow the user five "shots".
        click = win.getMouse()
        
        if(shot(click, shape1)):
            score += 9
            print("+9 points")
        elif(shot(click, shape2)):
            score += 7
            print("+7 points")
        elif(shot(click, shape3)):
            score += 5
            print("+5 points")
        elif(shot(click, shape4)):
            score += 3
            print("+3 points")
        elif(shot(click, shape5)):
            score += 1
            print("+1 point")

    win.getMouse()
    win.close()
            
    print("Your score is: ", score)                                     #Displays the users final score.   

    enter = input("Would you like to play again? y/n: ")                #Checks if the user would like to play again.
    if enter == 'y':
        main()
    else:
        print("Goodbye.")
main()
