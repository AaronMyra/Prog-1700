def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #input
    billAmount = input("Please Enter the Amount of the Bill: ")
    tax = 1.15
    tip = 0.2

    #Process
    taxedBill= int(billAmount) * tax
    tipAmount= int(billAmount) * tip
    finalBill= taxedBill + tipAmount

    #Output
    #print("Your bill is: ") + billAmount
    print("Your bill with tax is: {0}").format(taxedBill)) 
    print("Suggested tip amount is: {1}").format(tipAmount))
    print("Final total with tax and tip is: {2}").format(finalBill))


    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()