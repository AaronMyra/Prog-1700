#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Aaron Myra
Program Title:  Weekly Loan Calculator
Description:    Program to calculate the weekly payment of a loan
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    
    #input
    loanAmount=input("Enter the amount of loan: ")
    numberOfYears=input("Enter the number of years of loan repayment: ")
    intrestRate=input("Enter the intrest rate of loan (%): ")
    
    #Process
    intermediateValue= float(intrestRate)/5200
    weeklyPayment= float(intermediateValue)/(1-(1+float(intermediateValue))**(-52*float(numberOfYears)))*float(loanAmount)
    print("Your weekly repayment is: ${0:.2f}".format(weeklyPayment))
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()