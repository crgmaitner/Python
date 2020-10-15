import time                                                                        #Imports the time module.
print("This program displays a tree based on the users defined parameters.")
def main():
    x = int(input("Including the trunk, please provide a height for your tree: ")) #Requests the user enter a height for the tree.
    print("Your tree is now loading...")
    time.sleep(1)                                                                  #Pauses the program for one second to simulate loading.

    for i in range (x):                                                            #Begins for loop for the chosen tree height.
        print(((x-i-1)* ' '+(i*2+1)* '#'))                                         #Calculates the width of each branch based on the previous one.
                                                                                   #Also centers each branch.
    print((x-1)* ' '+'#')                                                          #Prints the trunk of the tree.
    print("Your tree has completed loading.")

    enter = input("Would you like to create another tree? y/n ")                   #Requests if user would like to create a new tree of a new height.

    if enter == 'y':                                                               #Executes if the user enters y, reverts to beginning of main.
        print("Follow the instructions to load a new tree.")
        main()
    else:                                                                          #Prints following statement if user enters n; program terminates.
        print("Goodbye.")

main()