#name2.py
#Craig Maitner

def main():
    print("This program calculates the numeric values of names taken from a file")
    print("and writes the results to a new file."'\n')
    infileData = input("Take names from: ")
    outfileData = input("Store name values in: ")
    
    infile = open(infileData, "r")
    outfile = open(outfileData, "w")
    
    for name in infile:
        sum = 0
        for ch in name[:-1].lower():
            sum = sum + ord(ch) - 96
        print(sum, file=outfile)

    print("The values have been written to the", outfileData,"file.")
    infile.close()
    outfile.close()
main()