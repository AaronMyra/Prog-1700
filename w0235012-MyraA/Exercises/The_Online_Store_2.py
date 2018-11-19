#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

#0 Variables
    totalBeforeTaxes = 0.0
    userCountry = ""
    userProvince = ""

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
        if userProvince == "nova scotia" or (userProvince == "new brunswick") or (userProvince == "ontario"):

            appliedTax = 0.15
            print("\n15% tax will be applied.")                
            
        # 4.2 If user is from Alberta
        elif userProvince == "alberta":
            
            appliedTax = 0.05
            print("\n5% tax will be applied.")
           
        
        # 4.3 If the user is from an other province
        else:
           
            appliedTax = 0.11
            print("\n11% tax will be applied.")
        
  
   # 5 If user is outside of canada
    else:

        appliedTax = 0
        print("\nNo taxes have been applied.")

    taxTotal = totalBeforeTaxes * appliedTax
    totalAmount = taxTotal + totalBeforeTaxes

    print("Tax: ${0:.2f}".format(taxTotal))
    print("Your total is ${0:.2f}".format(totalAmount))
    
    # 6 Outro
    print("Thank you for shopping!\n")



    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()