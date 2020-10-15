#chaos.py V4
#This program displays chaotic behavior.
#edited by Craig Maitner

def main():
    print("This program allows you to illustrate chaotic behavior.")
    x = eval(input("Enter a number between 0 and 10: "))
    n = eval(input("How many numbers should I print out?"))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)
		
main()