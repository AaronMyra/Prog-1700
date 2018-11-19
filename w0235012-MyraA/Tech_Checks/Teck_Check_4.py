############################################
# Tech Check 4 - Provided Starter File
############################################

#FUNCTION
def gradeCalculationProgram():

    def welcomeMessage():
        print("Grade Point Calculator\n")
        print("Valid letter grades that can be entered: A, B, C, D, F.")
        print("Valid grade modifiers are +, - or nothing.")
        print("All letter grades except F can include a + or - symbol.")
        print("Calculated grade point value cannot exceed 4.0.\n")
            
    def main(courseName):

        numericGrade = 0.0

        #Gather user inputs
        letterGrade = input("\nPlease enter a letter for {0} grade : ".format(courseName)).upper()
        modifier = input("Please enter a modifier (+, - or nothing) : ")

        # Determine base numeric value of the grade
        if letterGrade == "A":
            numericGrade = 4.0
        elif letterGrade == "B":
            numericGrade = 3.0
        elif letterGrade == "C":
            numericGrade = 2.0
        elif letterGrade == "D":
            numericGrade = 1.0
        elif letterGrade == "F":
            numericGrade = 0.0
        else:
            #If an invalid entry is made
            print("You entered an invalid letter grade.")
        
        # Determine whether to apply a modifier
        if modifier == "+":
            if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
                numericGrade += 0.3
        elif modifier == "-":
            if letterGrade != "F":     # Minus is not valid on F
                numericGrade -= 0.3
        return numericGrade

    def gradeOutput(courseName ,numericGrade):
        # Output final message and result, with formatting
        print("The numeric value for {0} is: {1:.1f}".format(courseName, numericGrade))

    welcomeMessage()
    
    course1 = "PROG1700"
    course2 = "NETW1700"
    course3 = "OSYS1200"
    course4 = "WEBD100"
    course5 = "COMM1700"
    course6 = "DBAS1001"

    userGrade1 = main(course1)
    userGrade2 = main(course2)
    userGrade3 = main(course3)
    userGrade4 = main(course4)
    userGrade5 = main(course5)
    userGrade6 = main(course6)

    gradeOutput(course1 ,userGrade1)
    gradeOutput(course2 ,userGrade2)
    gradeOutput(course3 ,userGrade3)
    gradeOutput(course4 ,userGrade4)
    gradeOutput(course5 ,userGrade5)
    gradeOutput(course6 ,userGrade6)


    numberOfCourses = 6
    gradeAverage = (userGrade1 + userGrade2 + userGrade3 + userGrade4 + userGrade5 + userGrade6) / numberOfCourses
    print("\n+---------------------------------------------+")
    print("|                                              |")
    print("|  Your overall grade point average is {0:.1f}      |".format(gradeAverage))
    print("|                                              |")
    print("+----------------------------------------------+\n")


    #PROGRAM STARTS HERE
    if __name__ == "__main__":
        return

gradeCalculationProgram()