#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Aaron Myra
Program Title:  Luggage Weight
Description:    Determines whether a surcharge is applied 
                based on client luggage weight
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    def paintShopProgram():

        #Intro
        print("\nWelcome to I.T. Airlines\n")

        #Input
        maxWeight=50.0
        surchargeAmount=25.00
        luggage_weight=float(input("\nPlease enter the weight of you luggage in Lbs: "))
        
        #Process
        if luggage_weight > maxWeight:
            print("Your luggage weight exceeds the maximum limit of 50lbs.")
            print("There is a ${0} surcharge\n".format(surchargeAmount))
            surchargeAnswer=input("Do you accept the surcharge? ").lower()
            if not surchargeAnswer=="yes":
                print("Please try again\n")
            else: 
                print ("\nThe surcharge will be applied") 
        else:
            print("\nYour luggage meets the requirements.")
        print("Thank you for flying I.T. Airlines.\n")
        return

    paintShopProgram()
        #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()