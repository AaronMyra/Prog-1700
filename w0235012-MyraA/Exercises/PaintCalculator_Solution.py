#Paint Shop Calculator
#Program to calculate the number of gallons of paint required to paint a room, if provided the room dimensions

def paintShopMainFunction():

    #Intro messages
    print("\nWelcome to the Paint Shop!")
    print("\nThis program will help you calculate how many cans of paint you need to buy, based on the dimensions of your room.")
    paintShopUserInput()

def paintShopUserInput():
    #INPUT
    #Get Dimensions of the room
    length = float(input("\nEnter the length of the room, in feet: "))
    width = float(input("Enter the width of the room, in feet: "))
    height = float(input("Enter the height of the room, in feet: "))
    paintShopCalculations(length, width, height)

def paintShopCalculations(length, width, height):

    #Import the math class, for using ceiling rounding
    import math

    #Declare variable for # of sq. ft. covered by one gallon of paint
    square_feet_per_gallon = 150
    .0

    #PROCESSING
    #Calculate the area of the walls
    totalArea = (length * height * 2) + (width * height * 2)

    #Divide the area by 150 square feet and
    #round number of gallons up to the nearest whole number
    gallons_of_paint = math.ceil(totalArea / square_feet_per_gallon)
    paintShopOutput(totalArea, gallons_of_paint)

def paintShopOutput(totalArea, gallons_of_paint):
    #OUTPUT - Display number of gallons needed
    print("\nThe total wall area of your room is {0} square feet.".format(totalArea))

    print("You will need {0} gallon(s) of paint. \n\nHappy Painting!\n".format(gallons_of_paint))
    return

paintShopMainFunction()










