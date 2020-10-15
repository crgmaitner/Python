import math
def main():
	print("This program calculates the cost per square inch of a circular pizza.")
	print()
	r = float(input("Provide a radius of your pizza: "))
	c = float(input("What is the cost of the pizza: "))
	area = math.pi * r ** 2
	total = area / c
	print("The cost per square inch of this pizza is: ",total)
main()