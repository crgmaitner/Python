#grade.py
#Craig Maitner

print("This program allows the user to enter an exam score and returns the corresponding letter grade.")

def main():
    score = int(input("Enter the exam score you received: "))

    if score > 100:
        print("That score is too high.")
    elif score > 90:
        score = 'A'
        print("You earned the grade: ", score)
    elif score > 80:
        score = 'B'
        print("You earned the grade: ", score)
    elif score > 70:
        score = 'C'
        print("You earned the grade: ", score)
    elif score > 60:
        score = 'D'
        print("You earned the grade: ", score)
    elif score > 0:
        score = 'F'
        print("You earned the grade: ", score)
    else:
        print("That score is too low.")

    choice = input("Would you like to convert another grade? y/n: ")

    if choice == 'y':
        print("Follow the instructions.")
        main()
    else:
        print("Goodbye.")
main()