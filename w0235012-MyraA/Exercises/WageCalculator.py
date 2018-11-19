#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Aaron Myra  
Program Title:  Wage Calculator 
Description:    Calculates weekly wage based on user iputs
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #Intro
    print("\nWelcome to the Wage Calculator")

    #Input
    overtimeHours=40.0
    overtimeAmount=1.5
    hoursWorked=float(input("\nEnter the number of hours you worked: "))
    wageAmount=float(input("Enter the amount you make per hour: $"))

    #Process
    if hoursWorked > overtimeHours:
        overTimeHoursWorked=hoursWorked-overtimeHours
        overTimeWage=wageAmount*overtimeAmount
        overWeeklyWage=(overTimeHoursWorked*overTimeWage)+((hoursWorked-overTimeHoursWorked)*wageAmount)
        print("\nThe amount you made this week is:\n${0:.2f}\n".format(overWeeklyWage))
    
    #Output
    else:
        weeklyWage=hoursWorked*wageAmount
        print("\nThe amount you made this week is:\n${0:.2f}\n".format(weeklyWage))


    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()