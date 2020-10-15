#functions.py
#Demonstrates the use of user created functions.

#Creates a new function called "sumN".
def sumN(x):
    sum = x * (x + 1) / 2
    return sum
#Creates a new function called "sumNCubes".
def sumNCubes(y):
    sum = (y * (y + 1) / 2) ** (1/3)
    return sum

#Begins the "main" function.
def main():
    print("This program demonstrates the use of two user created functions.")
    print("The first calculates a sum of the first n natural numbers, chosen by the user.")
    print("The second calculates a sum of the cubes of the first n natural numbers,") 
    print("again chosen by the user.")
    print()
    
    x = int(input("Enter a starting value: "))
    sumN(x)
    print("The sum of the first chosen natural numbers is: ", sumN(x))
    
    input("Press Enter to test the next function.")
    print()
    
    y = int(input("Enter a starting value: "))
    sumNCubes(y)
    print("The sum of the cubes of the first chosen natural numbers is: ", sumNCubes(y))
main()
