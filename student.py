#student.py
#Craig Maitner

def year(x):
    if x < 0:
        print("Not a student.")
    elif x < 7:
        print("You are classified as a Freshman.")
    elif x < 16:
        print("You are classified as a Sophomore.")
    elif x < 26:
        print("You are classified as a Junior.")
    else:
        print("You are classified as a Senior.")

def main():
    print("This program will accept a students credits and classify them based on the amount they have.")
    x = int(input("How many credits do you have: "))
    year(x)
    enter = input("Would you like to check again? y/n: ")
    if enter == "y":
        main()
    else:
        print("Goodbye.")
main()