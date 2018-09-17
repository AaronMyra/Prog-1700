#input
billAmount = input("Please Enter the Amount of the Bill: ")
tax = 1.15
tip = 0.2

#Process
taxedBill= float(billAmount) * tax
tipAmount= float(billAmount) * tip
finalBill= taxedBill + tipAmount

#Output
print("Your bill is: ") + billAmount
print("Your bill with tax is: ") + str(taxedBill) 
print("Suggested tip amount is: ")+ str(tipAmount)
print("Final total with tax and tip is: ")+ str(finalBill)