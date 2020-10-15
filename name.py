#name.py

def main():
    print("This program calculates the numeric value of a name that is provided by the user.")
    enter = input("Please give me a name: ")

    sum = 0
    for ch in enter.lower():
        sum = sum + ord(ch) - 96

    print("The sum of this name is: ", sum)
main()
