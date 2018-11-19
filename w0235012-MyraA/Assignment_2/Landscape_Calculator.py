#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Aaron Myra 
Program Title: Landscape Calculator 
Description:    Calculates a landscape estimate based on user 
                input of property area, desired grass type, desired number of trees.
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    
    # Calculations
    def totalAreaCalculations(p_propertyLength, p_propertyWidth):
        return p_propertyLength * p_propertyWidth

    def treeChargeCalculations(p_treeCharge, p_numberOfTrees):
        return p_treeCharge * p_numberOfTrees 

    def grassChargeCalculations(p_totalArea, p_grassCharge):
        return p_totalArea * p_grassCharge

    def totalAmountCalculations(p_grassChargeAmount, p_treeChargeAmount, p_labourCost):
        return p_grassChargeAmount + p_treeChargeAmount + p_labourCost
  
    # Landscape Calculator Main Function
    def landscapeCalculator():

        # 0 - Intro
        print("\nWelcome to the Landscape Calculator\n")
    
        # 1 - Variables
        maxAreaBeforeCharge = 5000
        treeCharge = 100
        grassCharge = 0.0
        exceedMaxAreaCharge = 500
        fescueCharge = 0.05
        bentgrassCharge = 0.02
        campusCharge = 0.01
        labourCost = 1000

   
        # 2 - Input
        userAddress = str(input("Enter the address: ")) #Ex. 123 Main St.
        propertyLength = float(input("Enter the total length of the property in feet: "))
        propertyWidth = float(input("Enter the total width of the property in feet: "))
        numberOfTrees = int(input("Enter the number of trees you would like: "))
        grassType = str(input("\nWe have 'fescue', 'bentgrass' and 'campus' grass types available.\nEnter the type of grass you would like: ")).lower()

        totalArea = totalAreaCalculations(propertyLength, propertyWidth)
        treeChargeAmount = treeChargeCalculations(treeCharge, numberOfTrees)

        # 4 - Area and Grass Type decisions
        if totalArea > maxAreaBeforeCharge:
            labourCost = labourCost + exceedMaxAreaCharge

        if grassType == "fescue":
            grassCharge = fescueCharge
        
        elif grassType == "bentgrass":
            grassCharge = bentgrassCharge

        elif grassType == "campus":
            grassCharge = campusCharge

        else:
            print("You have entered an invalid grass type. ")
            quit()

        grassChargeAmount = grassChargeCalculations(totalArea, grassCharge)
        totalAmount = totalAmountCalculations(grassChargeAmount, treeChargeAmount, labourCost)
        return userAddress, labourCost, treeChargeAmount, grassType, grassChargeAmount, totalAmount
 
    #Output Function
    def landscapeOutput(propertyEstimate):
        
        # 5 - Output
        print("\nThe cost for the landscape at '{[0]}' is as folows: ".format(propertyEstimate))
        print("\n    Labour Cost: {[1]}".format(propertyEstimate))
        print("    Cost for trees: {[2]}".format(propertyEstimate))
        print("    Type of grass: {[3]}".format(propertyEstimate))
        print("    Cost for grass: {[4]:.2f}\n".format(propertyEstimate))
        print("Total amount: ${[5]:.2f}\n".format(propertyEstimate))
    
    landscapeOutput(landscapeCalculator())

    #Your code ends on the line above.

#Do not change any of the code below!
if __name__ == "__main__":
    main()