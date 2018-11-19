#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Aaron Myra
Program Title:  Ewehon Mobile Data Plans
Description:    Calculates user mobile data rates for the Ewehon company.
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
 
    # Mobile Data Plan function
    def dataPlanProgram():

        #Intro
        print("\nWelcome to Ewehon Mobile.")
        print("Our data plans are based on customer data usage.")

        #Variables
        nullDataUsage = 0
        dataUsage = 0
        dataCharge = 0.0
        firstTeirDataRate = 20
        secondTeirDataRate = 0.105
        thirdTeirDataRate = 0.110
        forthTeirDataRate = 118
        firstTeirDataUsage = 200
        secondTeirDataUsage = 500
        thirdAndForthTeirDataUsage = 1024
   
        #Input
        dataUsage = int(input("\nEnter the amount of data used in megabytes: "))

        #if statements
        if dataUsage <= nullDataUsage:
            print("\nYou have entered an invalid data amount.\n")
            quit()
        elif dataUsage <= firstTeirDataUsage:
            dataCharge = firstTeirDataRate
        elif dataUsage <= secondTeirDataUsage:
            dataCharge = secondTeirDataRate * dataUsage
        elif dataUsage <= thirdAndForthTeirDataUsage:
            dataCharge = thirdTeirDataRate * dataUsage
        elif dataUsage > thirdAndForthTeirDataUsage:
            dataCharge = forthTeirDataRate
        else:
            print("You have entered an invalid data amount.\n")
            quit()
        
        return dataCharge

    # Output Function
    def mobilePlanOutput(p_dataCharge):
        # Program Execution 
        
        #Output
        print("\nYour amount for this billing cycle is: ${0:.2f}".format(p_dataCharge))

        #Outro
        print("Thank you for choosing Ewehon Mobile.\n")

    mobilePlanOutput(dataPlanProgram())

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()