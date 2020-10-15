# CMPT 120 Intro to Programming
# Chapter 11 lab: Lists and Error Handling
# Author: Your Name Here
# Created: YYYY-MM-DD


from __future__ import print_function
import os
import sys
import random
import time

# word database
Words = ['abcd','acbd','adbc']


# random choose
def getRandomWord():
    global Words
    return Words[random.randint(0, len(Words) - 1)]


# The function of guess word
def getGuess():
        for letter in word:
            letter = word.split()           #splits guess into each letter.
            for i in range (len(word)):
                if letter in wrongLetters:
                    print("The char: " + letter + " you have already guessed")

    #return letter


# The process to display results.
def displayGame(secretLetters, wrongLetters, secretWord):
    global guess
    global count
    print("Info: ")
    for letter in word:
        if letter in secretWord:
            secretLetters += letter
        else:
            wrongLetters += letter

    print("SecretLetters: ", end='')
    for letter in secretLetters:
        print(letter, end=' ')
    print()

    print("WrongLetters: ", end='')
    for letter in wrongLetters:
        print(letter, end=' ')
    print()
    print("Count: " + str(count))
    blanks = '_' * len(secretWord)
    for i in range(len(guess)):
        if i >= len(secretWord):
            break
        if secretWord[i] == guess[i]:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
    print("Word: ", end='')
    for i in blanks:
        print(i, end=" ")
    print()
    print()


# main process
def main():
    secretLetters = ''
    wrongLetters = ''
    secretWord = ''
    guess = ""
    count = 6

    os.system('cls')
    secretWord = getRandomWord()

    while True:
        displayGame(secretLetters, wrongLetters, secretWord)
        word = input("Guess the code: ")
        getGuess(word)
        if word == secretWord:
            print("You win !")
            break
        elif count <= 0:
            print("You lose !")
            break
        else:
            count -= 1
            continue


    result = input("do you want to play again?yes/no")
    if result == "yes":
        main()
    else:
        print("Thank you for playing")
main()