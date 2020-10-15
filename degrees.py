#degrees.py
    
print("This program will accept a sequence of values for temperature")
print("and output the running total of cooling and heating degree days.")
print('\n')

def main():
    temp = input("What are the average daily temperatures(,): ")
    temp = temp.split(",")
    
    cold=0
    hot=0

    try:
        for i in temp:
            if int(i) < 60 or int(i) > 80:
                if int(i) > 80:
                    cold= cold + (int(i)-80)
                else:
                    hot = hot + (60-int(i))
        print("The current estimate is", cold, "cooling degree days and", hot, "heating degree days.")
    
    except ValueError:
        print("Invalid input.")

    new = input("Would you like another estimate?(y/n): ")

    if new == "y":
        main()
    else:
        print("Run the program again to start a new estimate.")
if __name__ == '__main__':
    main()
