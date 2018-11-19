#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Aaron Myra
Program Title:  Weekly Loan Calculator
Description:    Program to calculate the weekly payment of a loan
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    
    #Intro
    print("\nThe Weekly Loan Calculator")

    #Input
    #Prompt the user to input data
    loanAmount=input("\nEnter the amount of loan: ")
    intrestRate=input("Enter the intrest rate of loan (%): ")
    numberOfYears=input("Enter the number of years of loan repayment: ")
    
    #Process
    intermediateValue= float(intrestRate)/5200
    weeklyPayment= float(intermediateValue)/(1-(1+float(intermediateValue))**(-52*float(numberOfYears)))*float(loanAmount)
    print("\nYour weekly payment is: ${0:.2f}\n".format(weeklyPayment))
    
    #Your code ends on the line above

#.Do not change any of the code below!
if __name__ == "__main__":
    main()