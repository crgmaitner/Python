# convert.py
# This program converts Celsius temperatures to Fahrenheit.
# edited by Craig Maitner

def main():
    print("This program can be used to easily convert from Celcius to Fahrenheit.")
    
    celsius = int(input("What is the Celsius temperature? "))
    fahrenheit = (9/5) * celsius + 32
    print("The temperature is ",fahrenheit," degrees Fahrenheit.")
    input("Press Enter to quit.")

main()