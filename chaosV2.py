#chaos.py V2
#This program displays chaotic behavior.
#edited by Craig Maitner

def main():
	print("This program allows you to illustrate chaotic behavior.")
	x = eval(input("Enter a number between 0 and 10: "))
	for i in range(20):
		x = 3.9 * x * (1 - x)
		print(x)
		
main()