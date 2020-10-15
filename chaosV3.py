#chaos.py V3
#This program displays chaotic behavior.

def main():
	print("This program allows you to illustrate chaotic behavior.")
	x = eval(input("Enter a number between 0 and 10: "))
	for i in range(10):
		x = 2.0 * x * (1 - x)
		print(x)
		
main()
