#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name: Aaron Myra      
Program Title:  Luggage Weight
Description:   Using the weight 
                of passenger's luggage it will 
                calculating wether a surcharge 
                will be applied  
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    print("Welcome to the I.T. Airlines\n")
    luggage_weight=float(input("\nPlease enter the weight of you luggage: "))
    if luggage_weight > 50:
        print("Your luggage weight exceeds the maximum limit of 50lbs.")
        print("There is a $25 surcharge")
        surchargeAnswer=input("Do you accept the surcharge? ").lower()
        if not surchargeAnswer == "yes":
            print("Please adjust and try again\n\n")
            main()
    else: print("Your luggage weight meets the requirements")
    print("\nThank You for flying I.T. Airlines\n\n\n")
    
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()