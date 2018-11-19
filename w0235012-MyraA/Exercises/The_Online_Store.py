#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Aaron Myra
Program Title:  The Online Store
Description:    Asks the user where they're fom and calculates taxes based on the input
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #0 Variables
    totalBeforeTaxes = 0.0
    userCountry = ""
    userProvince = ""
    albertaTax = 1.05
    eastCoastTax = 1.15
    otherProvinces = 1.11

    #1 Welcome
    print("\nWeclome to Canada's online store.\n ")

    #2 Promt user for country of residence
    totalBeforeTaxes = float(input("Enter the amount of your purchace: $"))
    userCountry = input("Enter the country you are from: ").lower()

    # 3 Determine Country
    # 4 If user is inside Canada
    if userCountry == "canada":
        userProvince = input("Enter the province you reside in: ").lower()
        
        # 4.1 If user is from Nova Scotia, Ontairo, New Brunswick
        if userProvince == "nova scotia":
            userProvince = True
        elif userProvince == "new brunswick":
            userProvince = True
        elif userProvince == "ontario":
            userProvince = True

        if userProvince == True:
            amountTotal = totalBeforeTaxes * eastCoastTax
            print("\n15% tax will be applied.")                
            print("You're total after taxes is ${0:.2f} CND. ".format(amountTotal))

        # 4.2 If user is from Alberta
        elif userProvince == "alberta":
            amountTotal = totalBeforeTaxes *  albertaTax
            print("\n5% tax will be applied.")
            print("You're total after taxes is ${0:.2f} CND. ".format(amountTotal))
        
        # 4.3 If the user is from an other province
        else:
            amountTotal = totalBeforeTaxes * otherProvinces
            print("\n11% tax will be applied.")
            print("You're total after taxes is ${0:.2f} CND. ".format(amountTotal))
  
   # 5 If user is outside of canada
    else:
        print("\nNo taxes have been applied.")
        print("Your total is ${0:.2f} CND.".format(totalBeforeTaxes))
    
    # 6 Outro
    print("Thank you for shopping!\n")

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()