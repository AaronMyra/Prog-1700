#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Aaron Myra
Program Title:  Restaurant_Bill
Description:    Calculate tip and tax on a resturant bill
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #input
    billAmount = input("Please Enter the Amount of the Bill: ")
    tax = 0.15
    finalTax = 1.15
    tip = 0.2

    #Process
    taxOfBill= float(billAmount) * tax
    tipAmount= float(billAmount) * tip
    taxedBill = float(billAmount) * finalTax
    finalBill= taxedBill + tipAmount

    #Output
    print("Your original bill is: $" + billAmount)
    print("Tax of your bill is: ${0:.2f}".format(taxOfBill))
    print("Suggested tip amount is: ${0:.2f}".format(tipAmount))
    print("Final total with tax and tip is: ${0:.2f}".format(finalBill))


    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()