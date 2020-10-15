import math
def main():
	print("This program computes the molecular weight of a carbohydrate.")
	print()
	H = 1.0
	C = 12.0
	O = 16.0
	
	valx = int(input("How many Hydrogen atoms: "))
	valy = int(input("How many Carbon atoms: "))
	valz = int(input("How many Oxygen atoms: "))
	
	weight = (valx*H) + (valy*C) + (valz*O)
	
	print("The total combined molecular weight of this atom is: ", weight)
main()