#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name: Aaron Myra   
Program Title:  Hipster's Vinyl Records
Description:    Calculating Cost, Delivery, and Tax For a Record Store
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #input
    deliveryCharge=15 #dollars pre kilometer
    tax=1.14
    custName=input("Please Enter Cutomer's Name: ")
    deliveryDistance=input("Enter the distance to the delivery in kilometers: ")
    recordCost= input("Enter the cost of an records purchased: ")

    #Process
    deliveryCost= float(deliveryDistance) * deliveryCharge
    taxedCost= float(recordCost) * tax
    finalTotal= deliveryCost + taxedCost

    #Output
    print("Hipster's Local Vinyl Records Recipt")
    print("Customer's Name: " + custName)
    print("Delivery Cost: ${0:.2f}".format(deliveryCost))
    print("Cost of records with tax: ${0:.2f}".format(taxedCost))
    print("Total cost is: ${0:.2f}".format(finalTotal))
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()