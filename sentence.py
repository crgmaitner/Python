#sentence.py
#Craig Maitner

print("This program will accept a sentence of any length and return some general information about it.")

def main ():
    sentence= input("Please enter your sentence here: ").lower()                    #Gets a sentence as input from the user.
    
    num=len(sentence)                                                               #Returns the number of characters in the sentence.
    print("Number of characters: ", num)
    
    wordCount=len(sentence.split())                                                 #Returns the number of words in the sentence.
    print("Number of words: ", wordCount)
    
    average = int(num/wordCount)                                                    #Calculates the average word length within the
    print("Average word length: ", average)                                         #sentence, then returns that value.
    
    new = input("Would you like to analyze another sentence? y/n: ")                #Checks if the user would like to analyze a new
                                                                                    #sentence.
    if new == 'y':
        print("Follow the instructions to analyze a new sentence.")
        main()
    else:
        print("Goodbye.")
main()