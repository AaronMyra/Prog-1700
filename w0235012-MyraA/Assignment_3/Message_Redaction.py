#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Aaron Myra
Program Title:  Message Redaction
Description:    Removes specified letter values from user inputted sentence
"""

# Functions
#------------------------------------------------------------------#
# Replace letters fron user inputted comma list in phrase with "_"
def redactMessage(p_userCommaList, p_userInput):
    for counter in range(len(p_userCommaList)):
        if p_userCommaList[counter] in p_userInput and p_userCommaList[counter] != "," and p_userCommaList[counter] != " ":
            p_userInput = p_userInput.replace(p_userCommaList[counter], "_")
    return p_userInput

# Quits program if user enters "quit"
def quitInput(p_userInput):
    if p_userInput.lower() == "quit":
            print("\nGoodbye.\n")
            quit()

# Checks user inputs for any digits
def errorChecking(p_input):
    for counter in range(len(p_input)):
            if  p_input[counter].isdigit():
                print("\nError! you have entered an invalid value. Please try again.")
                main()

# Welcome message
print("\nWelcome to the message redaction program.")

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    userInput = ""

    # Repeat program until the user enters "Quit"
    while userInput.lower() != "quit":

        # Prompt user to enter a phrase
        userInput = input("\nEnter a phrase or 'Quit' to exit:  ")

        # Checks user inputs for any digits
        errorChecking(userInput)
        
        # Quits program if user enters "quit"
        quitInput(userInput)
        
        # Prompt user to enter comma-seperated list of letters
        userCommaList = input("Enter a comma-seperated list of letters to redact: ")

        # Checks user inputs for any digits
        errorChecking(userCommaList)

        # Replace letters fron user inputted comma list in phrase with "_"
        userInput = redactMessage(userCommaList, userInput)

        # Output
        print("\nNumber of letters redacted: {0}.".format(userInput.count("_")))   
        print(userInput)

    #Your code ends on the line above.

#Do not change any of the code below!
if __name__ == "__main__":
    main()