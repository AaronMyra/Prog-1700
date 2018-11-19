#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:  Aaron Myra  
Program Title:  The A-Team
Description:    Takes the original A-Team intro and adds line numbers, omits a random line based on a random number generator,
                and chanmges lines with more than 20 characters to lowercase and lines with less than 20 characters to uppercase.
"""

def lineBreakFunction():
    print("\n")

def appendNewFileFunction(p_newFileName, p_accessMode, p_content):
    newATeamFile = open(p_newFileName, p_accessMode)
    newATeamFile.write(p_content + "\n") 

def omitRandomLineFunction(p_lineNumber, p_randomNumber, p_row):
    if p_lineNumber != p_randomNumber:
        p_alteredRow = p_row 
    else:
        p_alteredRow = ""
    return p_alteredRow

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #Import Functions
    import random

    #Initalize Variables
    originalFileName ="Assignment_4\A-Team_Intro_Program\P1 - ateam_Original.txt"
    newFileName = "Assignment_4\A-Team_Intro_Program\P1 - ateam_Altered.txt"
    appendAccessMode = "a"
    readAccessMode = "r"
    writeAccessMode = "w"
    aTeamTextList = []
    lineNumber = 0
    characterCount = 0
    originalTextTitle = "Original Text"
    alteredTextTitle = "Altered Text"
    dottedLineBorder = "----------------------\n"
    alteredRow = ""
    counter = 0
    maxCharacters = 20

    #Open and read ateam orginal text file
    try:
        aTeamFile = open(originalFileName, readAccessMode)
        aTeamText = aTeamFile.read()
        aTeamTextList = aTeamText.split("\n")
    except FileNotFoundError:
        print("\nError! The file 'P1 - ateam_Original.txt' was not found. Please try again.\n")
        quit()


    #Print Original Text
    print("\n" + originalTextTitle)
    print(dottedLineBorder)
    appendNewFileFunction(newFileName, writeAccessMode, originalTextTitle)
    appendNewFileFunction(newFileName, appendAccessMode, dottedLineBorder)
    for row in aTeamTextList:
        print(row, end="\n")
        appendNewFileFunction(newFileName, appendAccessMode, row)
    lineBreakFunction()

    #Altered Text
    print(alteredTextTitle)
    print(dottedLineBorder)
    appendNewFileFunction(newFileName, appendAccessMode, "\n" + alteredTextTitle)
    appendNewFileFunction(newFileName, appendAccessMode, dottedLineBorder)

    #Generate random number
    randomNumber = random.randint(1, 10)
    for row in aTeamTextList:
        
        #If line number is equal to randomly generated number omit from output
        lineNumber += 1
        alteredRow = omitRandomLineFunction(lineNumber, randomNumber, row)

        #If row contains more than 20 characters output it in lowercase
        characterCount = 0
        for column in alteredRow: 
            # if column.isalpha and column != " ":
            characterCount += 1
            if characterCount > maxCharacters:
                alteredRow = row.lower()
                counter += 1
            else:
                alteredRow = row.upper()
                counter += 1

        #Append altered text to new file and print to console
        
        if alteredRow != "":
            appendNewFileFunction(newFileName, appendAccessMode,"line {0}: {1}".format(lineNumber, alteredRow))
            print("line {0}: {1}".format(lineNumber, str(alteredRow)))
        else:
            appendNewFileFunction(newFileName, appendAccessMode,"")
            print("")
       
    lineBreakFunction()

    #Close File
    aTeamFile.close()

    #Your code ends on the line above.

#Do not change any of the code below!
if __name__ == "__main__":
    main()