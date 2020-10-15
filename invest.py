#invest.py

import math

def main():
    print("This program will calculate an investment based on an interest rate.")
    invest = int(input("What is the principle: "))
    rate = float(input("At what interest rate: "))
    end = invest

    time = 0
    while end <= (2 * invest):
        time = time + 1
        end = end * (1 + (rate))
    print("This investment will double in: ", time, "years.")
main()
