import math
def main():
	print("This program calculates the cost of a coffee order.")
	
	A = float(input("Enter the amount of coffee you would like to purchase: "))
	cp = A * 10.5
	print(A," pounds of coffee will cost ", cp)
	shipping = (0.86*A) + 1.5
	total = cp + shipping
    
	print("This order of coffee will cost you ", total)
main()