import math
def main():
    print("This program calculates the sum of natural numbers.")

    n = int(input("Enter a whole, natural number: "))

    sum = 0
    for factor in range(1, n+1):
        sum = sum + factor

    print("The sum of these numbers is: ", sum)
main()