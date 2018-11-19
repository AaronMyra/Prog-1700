#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Aaron Myra 
Program Title:  Grade Calculator
Description:    Calculates grades based on user input
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

 #Intro
    print("\nWelcome to the Grade Calculator")

    #Variables
    letterGrade = ""
    letterModifier = ""


    #Input
    letterGrade = input("\nEnter your letter grade (A to F): ").lower()
    letterModifier = input("Enter '+' or '-' if they apply to the letter grade: ")
    numericGrade = 0.0
    gradeModifier = 0.3

    #Process
    # Setting numeric grade based on letter grade
    if letterGrade == "a":
         numericGrade = 4.0
    elif letterGrade == "b":
        numericGrade = 3.0
    elif letterGrade == "c":
        numericGrade = 2.0
    elif letterGrade == "d":
        numericGrade = 1.0
    elif letterGrade == "f":
        numericGrade = 0.0
    else:
        print("\nYou have entered an invaild grade.")
        %reset?
        main()

    # Adjusting grade based on modifier
    if letterModifier == "+":
        numericGrade = numericGrade + gradeModifier
    elif letterModifier == "-":
        numericGrade = numericGrade - gradeModifier
    
    # setting letter "A" and "F" grade
    if letterGrade == "a":
         numericGrade = 4.0
    elif letterGrade == "f":
        numericGrade = 0.0
    
    #Output
    print("\nYou entered '{0}' as the letter grade".format(letterGrade.upper()))
    print("The corresponding numeric grade is: {0}\n".format(numericGrade))


    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()