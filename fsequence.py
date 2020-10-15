#fsequence.py
#Craig Maitner
import math

def main():
    print("This program will output the nth Fibonacci number based on a value entered by the user.")
    n = int(input("Enter a value: "))

    number = 0
    prev = 0
    for i in range(n + 1):
        #number = (n - 1) + (n - 2)
        print(number, prev)
        if i == 0:
            number += 0
        elif i == 1:
            number += 1
        else:
            number += prev
            prev = number

    print("The Fibonacci number is: ", number)
main()