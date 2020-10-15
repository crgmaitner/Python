#censor.py
#Craig Maitner

#Defines a new function called "secret"
def secret(word):
    # Replaces each letter or number in the word with an asterisk '*'
    for i in range(len(word)):
        if word[i].isalpha() or word[i].isnumeric():
            word = word[:i] + '*' + word[i+1:]
    return word
    
print("This program accepts a text file as input and censors some of the words within it")
print("based on a second text file."'\n')

def main():
    inData = input("Censor which file: ")
    wordData = input("Words to censor: ")
    outData = input("Write to what new file: ")

    ##################################
    # Opens the inData File as inFile
    # Gets the text of inFile as inText
    # Splits inText at each line break
    ##################################
    inFile = open(inData, 'r')
    inText = inFile.read()
    inLines = inText.split('\n')

    ####################################
    # Opens the wordDate File as wordFile
    # Gets the text of wordFile as wordText
    # Splits wordText at each line break
    ####################################
    wordFile = open(wordData, 'r')
    wordText = wordFile.read()
    wordLines = wordText.split('\n')

    # Open outData File as outFile
    outFile = open(outData, 'w')

    # Creates a new string for censored line
    secret_line = ''
    
    for line in inLines:
        # Splits the line at each space
        words = line.split()

        for i in range(len(words)):
            # Creates a new string for the censored word
            word = ''

            # Adds only letters or numbers to censored word
            for ch in words[i]:
                if ch.isalpha() or ch.isnumeric():
                   word += ch
            
            if word in wordLines:
                words[i] = secret(words[i])

        # Adds each word to censored line separated by spaces
        secret_line += ' '.join(words) + '\n'

    # Write secret_line to outFile
    outFile.write(secret_line)

    # Close all files
    print("The file has been censored.")
    inFile.close()
    wordFile.close()
    outFile.close()
    
    newfile = input("Would you like to encrypt another file? y/n: ")
    if newfile == 'y':
        print('\n'"A new file will now be encrypted.")
        main()
    else:
        print("Goodbye.")
if __name__ == '__main__':
    main()