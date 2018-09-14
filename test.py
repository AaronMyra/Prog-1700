def main ():
    
    #input: values from user and amount of space 1 gallon paint covers
    pairsOfWalls= 2
    paintPerSquareFoot = 150
    widthOfWall1= input("What is the width of wall 1? ")
    widthOfWall2= input("What is the width wall 2? ")
    heightOfWalls=input("What is the height of the walls? ")
    #heightOfWall2= input("What is the height of wall 2?") redundant?
    
    #Process: Calculation of room area, and gallons needed
    wallArea1= float(widthOfWall1) * float(heightOfWalls)
    wallArea2= float(widthOfWall2) * float(heightOfWalls)
    wallArea1= wallArea1 * pairsOfWalls
    wallArea2= wallArea2 * pairsOfWalls
    roomArea= wallArea1 + wallArea2
    gallonsOfPaint= roomArea / paintPerSquareFoot
    
    #Output: Displaying the gallons of paint needed
    if int(gallonsOfPaint) < 1:
       print("Gallons of paint required: 1")
    else:  
        print("Gallons of paint required:",int(gallonsOfPaint))

    #Extra
    costOfGallon= input("What is the cost of paint per gallon? ")
    total= int(costOfGallon) * gallonsOfPaint
    print ("total:"+" $"+str(total))
main ()