#ticket.py

def main():
    print("This program will calculate a speeding ticket based on how fast a driver was going.")
    speed = int(input("How fast was the driver going: "))
    limit = int(input("What is the speed limit: "))
    
    if speed < limit:
        print("This speed is legal.")
    else:
        print("This speed is illegal.")
        fine = 50 + (5 * (speed - limit))
        if speed > 90:
            fine = fine + 200
        print("Your ticket amount is: ", fine)
main()
