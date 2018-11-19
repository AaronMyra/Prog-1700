#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Aaron Myra
Program Title:  The Itsy Bitsy Aardvark
Description:    Replaces certin values in a text file based on user input
"""
#User choice error handling function
def userChoiceError(p_userLetterChoice, p_choiceLetterList, p_row):
    if p_userLetterChoice in p_choiceLetterList:
        choiceIndex = p_choiceLetterList.index(p_userLetterChoice)
        p_userChoice = p_row[choiceIndex + 1]
        return p_userChoice

#Replace placeholer with user selected value function
def replaceFunction(p_FileText, p_oldValue, p_newValue):
    p_alteredStory = p_FileText.replace(p_oldValue, p_newValue)
    return p_alteredStory

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #Intro
    print("\nWelcome To The Itsy Bitsy Aardvark Mad-Lib ")

    #Import CVS
    import csv

    #Initalize Variables
    numberOfLines = 7
    choicesFileName = "Assignment_4/Mad_Lib_Program/the_choices_file.csv"
    storyFileName = "Assignment_4/Mad_Lib_Program/the_story_file.txt"
    readAccessMode = "r"
    columnNumber = 0
    choiceLetterList = ["a", "b", "c", "d", "e"]
    counter = 0
    userChoiceList = []
    replaceList = ["_1_", "_2_", "_3_", "_4_", "_5_", "_6_", "_7_"]

    #Open "the_story_file"
    try:
        storyFile = open(storyFileName, readAccessMode)
        storyFileText = storyFile.read()
        storyFileList = storyFileText.split(" ")
    except FileNotFoundError:
        print("\nError! The file 'the_story_file.txt' was not found. Please try again.\n")
        quit()

    #Open "the_choices_file" CSV file
    try:
        choicesCSV_File = open(choicesFileName, readAccessMode)
        choicesFileData = csv.reader(choicesCSV_File, delimiter = ",")
    except FileNotFoundError:
        print("\nError! The file 'the_choices_file.csv' was not found. Please try again.\n")
        quit()

    for row in choicesFileData:

        #Set counters back to 0 
        columnNumber = 0
        counter = 0

        #Display the category and choices
        for column in row:
            if columnNumber < 6:
                if columnNumber == 0:
                    print("\nPlease Choose {0}".format(column))
                else:
                    print("({0}) {1}".format(choiceLetterList[counter], column))
                    counter += 1
            columnNumber += 1
        
        #Prompt the user to input a choice
        userLetterChoice = input("Enter choice (a-e): ").lower()
        userChoice = userChoiceError(userLetterChoice, choiceLetterList, row)

        #Error check if user entered a vaild character
        if userLetterChoice in choiceLetterList:
            userChoiceList.append(userChoice.upper())
        
        #If user did not enter a valid character repeat input until they do
        while not userLetterChoice in choiceLetterList:
            print("\nError! You have entered an invalid letter. Please try again.")
            userLetterChoice = input("Enter choice (a-e): ").lower()
            if userLetterChoice in choiceLetterList:
                userChoice = userChoiceError(userLetterChoice, choiceLetterList, row)
                userChoiceList.append(userChoice.upper())

    #Replace the placeholder with the user input
    alteredStory = storyFileText
    # alteredStory = replaceFunction(storyFileText, replaceList[0], userChoiceList[0])
    for index in range(numberOfLines):
        alteredStory = replaceFunction(alteredStory, replaceList[index], userChoiceList[index])

    #Output the altered story
    print("\n" + alteredStory)
    print("\nFIN\n")

    #Close file
    storyFile.close()
                
    #Your code ends on the line above.

#Do not change any of the code below!
if __name__ == "__main__":
    main()