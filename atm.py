#atm.py
#Craig Maitner
#username: crgma    pin:2468

# This list will hold the account info.
# account_info[0] = userID
# account_info[1] = Pin
# account_info[2] = Checking Balance
# account_info[3] = Savings Balance
account_info = []

#Defines a new function to get the balances of each account that is connected to this username and pin.
def getBalances():
    print()
    print("Checking: $" + account_info[2])
    print("Savings: $" + account_info[3])

#Creates a new function called "deposit" to allow the user to deposit funds into either account.
def deposit(depositAmount):
    print("c. Checking")
    print("s. Savings")
    userChoice = input("Which Account Would You Like to Deposit Into: ")

    if userChoice == "c":
        currBalance = int(account_info[2])
        newBalance = currBalance + depositAmount
        account_info[2] = str(newBalance)
        print(depositAmount, "dollars has been deposited into Checking.")
    elif userChoice == "s":
        currBalance = int(account_info[3])
        newBalance = currBalance + depositAmount
        account_info[3] = str(newBalance)
        print(depositAmount, "dollars has been deposited into Savings.")
    else:
        print("Select an appropriate account to deposit into.")
        deposit(depositAmount)

#Creates a new function called "withdraw" to allow the user to withdraw funds from either account.
def withdraw(withdrawAmount):
    print("c. Checking")
    print("s. Savings")
    userChoice = input("Which Account Would You Like to Withdraw From: ")

    if userChoice == "c":
        currBalance = int(account_info[2])
        if currBalance >= withdrawAmount:
            newBalance = currBalance - withdrawAmount
            account_info[2] = str(newBalance)
            print(withdrawAmount, "dollars has been withdrawn from Checking.")
        else:
            print("Insufficient Funds")
    elif userChoice == "s":
        currBalance = int(account_info[3])
        if currBalance >= withdrawAmount:
            newBalance = currBalance - withdrawAmount
            account_info[3] = str(newBalance)
            print(withdrawAmount, "dollars has been withdrawn from Savings.")
        else:
            print("Insufficient Funds")
    else:
        print("Select an appropriate account to withdraw from.")
        withdraw(withdrawAmount)

#Creates a new function called "transfer" to all the user to transfer funds between  accounts.
def transfer(transferAmount):
    print("c. Checking")
    print("s. Savings")
    userChoice = input("From which account would you like to transfer funds: ")

    if userChoice == "c":
        currBalance = int(account_info[2])
        if currBalance >= transferAmount:
            newBalance = currBalance - transferAmount
            account_info[2] = str(newBalance)
            sBalance = int(account_info[3]) + transferAmount
            account_info[3] = str(sBalance)
            print(transferAmount, "dollars has been transferred from Checking to Savings.")
        else:
            print("Insufficient funds.")
    elif userChoice == "s":
        currBalance = int(account_info[3])
        if currBalance >= transferAmount:
            newBalance = currBalance - transferAmount
            account_info[3] = str(newBalance)
            cBalance = int(account_info[2]) + transferAmount
            account_info[2] = str(cBalance)
            print(transferAmount, "dollars has been transferred from Savings to Checking.")
        else:
            print("Insufficient funds.")

# Main ATM Menu
def atmMenu():
    userChoice = "0"
    while(userChoice != "5"):
        print()
        print("Main Menu")
        print("1. Balance Inquiry")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Log Off")
        userChoice = input("What would you like to do: ")

        if userChoice == "1":
            getBalances()
        elif userChoice == "2":
            #Each "try" block will try the following code with the given user input.
            #Each "except" block will catch a ValueError to ensure that the user has
            #entered an input of a valid type.
            try:
                depositAmount = int(input("Enter Deposit Amount: "))
                deposit(depositAmount)
            except ValueError:
                print("You must enter an amount to deposit.")
        elif userChoice == "3":
            try:
                withdrawAmount = int(input("Enter Withdraw Amount: "))
                withdraw(withdrawAmount)
            except ValueError:
                print("You must enter an amount to withdraw.")
        elif userChoice == "4":
            try:
                transferAmount = int(input("Enter Transfer Amount: "))
                transfer(transferAmount)
            except ValueError:
                print("You must enter an amount to transfer.")
        elif userChoice == "5":
            print("Thank you for banking with us.")
        else:
            print("Please Choose a Number Between 1 and 5.")
    
def main():
    # Create inData string which is filename
    inData = "account.txt"
    # Open inData File as inFile
    inFile = open(inData, 'r')
    # Get text of inFile as inText
    inText = inFile.read()
    # Split inText at each line break
    inLines = inText.split('\n')
    # Close inFile
    inFile.close()

    for line in inLines:
        # Only look at line if it has ':' in it
        if ':' in line:
            # Split line into array before and after ": "
            line_details = line.split(": ")
            # Take second entry in array (after ": ")
            line_detail = line_details[1]
            # Add this to account_info
            account_info.append(line_detail)

    # Get ID and Pin from user
    print("Welcome to Python's Bank.")
    print("Please enter your username and pin number.")
    userID = input("\nUsername: ")
    userPin = input("Pin: ")

    # Access atmMenu if userID and userPin match ID and PIN
    if userID == account_info[0] and userPin == account_info[1]:
        print("Successful Login")

        # Run the ATM Menu Logic
        atmMenu()

        # Create new_account based on transactions done in ATM Menu
        new_account = "ID: " + account_info[0] + "\n"
        new_account = new_account + "Pin: " + account_info[1] + "\n"
        new_account = new_account + "\n"
        new_account = new_account + "Checking: " + account_info[2] + "\n"
        new_account = new_account + "Savings: " + account_info[3]

        # Open inData File as outFile
        outFile = open(inData, 'w')
        # Write new_account to outFile
        outFile.write(new_account)
        # Close outFile
        outFile.close()
    else:
        print("Incorrect Username or Pin.")

if __name__ == '__main__':
    main()