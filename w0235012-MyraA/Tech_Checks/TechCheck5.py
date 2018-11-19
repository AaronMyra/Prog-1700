#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Aaron Myra
Program Title:  Highest common divisor
Description:    Finds the highest common divisor between two user inputted numbers
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    tryAgain = "Y"

    while tryAgain != "N":

        userInputList = []

        for counter in range(2):
            userInput = input("\nEnter number {0}: ".format(counter + 1))
            if userInput.isnumeric():
                userInputList.append(int(userInput))

            else:
                while not userInput.isnumeric():
                    print("\nThats not a valid number. Please try again.")
                    userInput = input("\nEnter number {0}: ".format(counter + 1))
                    if userInput.isnumeric():
                       userInputList.append(int(userInput))
        
        def getHighestComonDivisor(p_userInputList):
            
            for innerCounter in range(1, min(p_userInputList) + 1):

                    if (p_userInputList[0] % innerCounter) == 0 and (p_userInputList[1] % innerCounter) == 0:
                        highestComonDivisor = innerCounter

            return highestComonDivisor

        print("\nThe highest common divisor of {0} and {1} is {2}.".format(userInputList[0], userInputList[1], getHighestComonDivisor(userInputList)))

        tryAgain = input("\nWould you like to try again (Y/N): ").upper()

        while tryAgain != "Y" and tryAgain != "N":
            print("\nERROR! You entered an in valid letter. Please try again")
            tryAgain = input("\nWould you like to try again (Y/N): ").upper()

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()