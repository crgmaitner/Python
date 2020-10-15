#pay.py
#Craig Maitner

def main():
    print("This program will calculate the total wages based on hourly rate")
    print("and the number of hours worked for that week.")
    print(" ")

    hours = float(input("How many hours did you work this week: "))
    pay = float(input("What is your hourly rate: "))
    
    salary = hours * pay
    
    if hours > 40:
        othours = hours - 40
        salary = 40 * pay + (othours * pay * 1.5)
        print("Awesome! You earned overtime pay this week!")
    else:
        print("You did not earn any overtime pay this week.")

    print("Your total wage for this week is: ", salary)
main()