import math
def main():
	print("This program calculates the volume and surface area of a sphere from a given radius.")

	r = float(input("Please provide a radius: "))
	V = 4 / (3*math.pi)*(r**3)
	A = (4*math.pi)*(r**2)

	print("The volume is: ", V)
	print("The area is: ", A)
main()