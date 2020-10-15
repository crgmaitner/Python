import math
def main():
    print("This program computes the distance to a lightning strike.")
    t = float(input("Time passed between flash and thunder in seconds: "))
    
    distance = t * 5500
    miles = distance / 5280

    print("The distance to the lightning strike in feet is: ",distance)
    print("This distance in miles is: ", miles)
main()