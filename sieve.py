#sieve.py
#Craig Maitner

#This function demonstrates the Sieve of Eratosthenes algorithm to find all primes up to a given limit value
def prime(n):
    a = []
    b = []
    for x in range(2,n+1):
        if x not in a:
            b.append(x)
            for y in range(x*x,n+1,x):
                a.append(y)
    return b

def main():
    print("This program uses a function to find all primes less than or equal to a given value. \n")
    value = int(input("Enter a whole number value: "))

    #Calls the prime function using the provided value as input.
    prime(value)
    
    #Checks if the value entered is less than or equal to 2; printing appropriate output.
    if value <= 2:
        print("No primes to compute. 2 is the first prime number.")
    else:
        print("The primes less than or equal to this value are: ", prime(value))
main()