#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Aaron Myra
Program Title:  Auto Insurance Calculator
Description:    Calculates auto insurance cost based on user biological sex, age and taxable income
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    # Insurance Calculations Function
    def insuranceCalculation(p_insuranceTeirRate, p_userVehicleCost, p_monthsInYear):
            insuranceTotal = (p_insuranceTeirRate * p_userVehicleCost) / p_monthsInYear
            return insuranceTotal

    def invalidAgeMessage():
        print("\nYou have entered and invalid age.\n")
        quit()
   
    # Main Program Function
    def insuranceProgram():

        #Intro
        print("\nWelcome to I.T. Auto Insurance.")

        #Variables
        userSex = ""
        userAge = 0
        userVehicleCost = 0.0
        monthsInYear = 12

        #Variables - Male
        firstTeirMaleRate = 0.25
        secondTeirMaleRate = 0.17
        thirdTeirMaleRate = 0.1

        #Variables - Female
        firstTeirFemaleRate = 0.2
        secondTeirFemaleRate = 0.15
        thirdTeirFemaleRate = 0.1
        

        #Input
        userSex = input("\nEnter your biological sex (M or F): ").upper()
        userAge = int(input("Enter your age: "))
        userVehicleCost = float(input("Enter the cost of the vehicle: "))

        #if statements
        #Male
        if userSex == "M":
            if userAge >= 70:
                invalidAgeMessage()
            elif userAge >= 40:
                insuranceTotal = insuranceCalculation(thirdTeirMaleRate, userVehicleCost, monthsInYear)
            elif userAge >= 25:
                insuranceTotal = insuranceCalculation(secondTeirMaleRate, userVehicleCost, monthsInYear)
            elif userAge >= 15:
                insuranceTotal = insuranceCalculation(firstTeirMaleRate, userVehicleCost, monthsInYear)
            elif userAge <= 14:
                invalidAgeMessage()

        #Female
        elif userSex == "F":
            if userAge >= 70:
                invalidAgeMessage()
            elif userAge >= 40:
                insuranceTotal = insuranceCalculation(thirdTeirFemaleRate, userVehicleCost, monthsInYear)
            elif userAge >= 25:
                insuranceTotal = insuranceCalculation(secondTeirFemaleRate, userVehicleCost, monthsInYear)
            elif userAge >= 15:
                insuranceTotal = insuranceCalculation(firstTeirFemaleRate, userVehicleCost, monthsInYear)
            elif userAge <=14:
                invalidAgeMessage()

        #Other
        else:
            print("\nYou have entered an invalid value.")
            quit()
        
        return insuranceTotal
          
    #Output Function
    def insuranceOutput():

        #Output
        print("\nYour insurance rate per month is: ${0:.2f}".format(insuranceProgram()))

        #Outro
        print("Thank you for choosing I.T. Auto Insurance.\n")
        return

    insuranceOutput()
    

    #Your code ends on the line above.

#Do not change any of the code below!
if __name__ == "__main__":
    main()