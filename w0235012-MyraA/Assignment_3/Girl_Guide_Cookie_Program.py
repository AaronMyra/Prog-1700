#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Aaron Myra
Program Title:  Girl Guide Cookie Program
Description:    User enters guides name and amount of cookies sold and program determines whether/which corisponding prize is awarded
"""

# Functions
# Guide Name Input Function
def guideNameInput(p_guidesNamesList, p_counter):
    guideName = input("\nEnter the name of guide #{0}: ".format(p_counter + 1)).capitalize()
    if guideName.isalpha():
        p_guidesNamesList.append(guideName)
    else:
        print("\nError! You have entered an invalid name. Please try again.")
        guideNameInput(p_guidesNamesList, p_counter)
    return p_guidesNamesList

# Guide cookies sold function
def guideCookiesSold(p_numberOfCookiesSold, p_guidesNamesList, p_counter):
    cookiesSold = input("Enter the number of boxes of cookies sold by {0}: ".format(p_guidesNamesList[p_counter]))
    if cookiesSold.isdigit():
        p_numberOfCookiesSold.append(int(cookiesSold))
    else:
        print("\nError! You have entered an invalid number of boxes. Please try again.")
        guideCookiesSold(p_numberOfCookiesSold, p_guidesNamesList, p_counter)
    return p_numberOfCookiesSold

# Prize awarded output function
def guidePrizeAwarded(p_guidesNamesList, p_counter, p_prizeList, p_prizePosition):
    print("{0}\t\t-{1}".format(p_guidesNamesList[p_counter], p_prizeList[p_prizePosition]))

# Welcome Message
print("\nWelcome to the Girl Guide Cookie Program.") 
  
def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    numberOfGuides = input("\nEnter the number of guides selling cookies: ")

    #Error Checking
    if numberOfGuides.isdigit():
        numberOfGuides = int(numberOfGuides)

        #Initlize Variables
        guidesNamesList = []
        numberOfCookiesSold = []
        averageBoxesSold = 0
        prizeList = ["Trip to the Girl Guide Jamboree in Aruba", "Super Seller Badge", "Split the remaining cookies", ""]

        for counter in range(numberOfGuides):

            guideNameInput(guidesNamesList, counter)
            guideCookiesSold(numberOfCookiesSold, guidesNamesList, counter)
            averageBoxesSold = (averageBoxesSold + numberOfCookiesSold[counter])
        
        averageBoxesSold = averageBoxesSold / numberOfGuides

        # Output
        print("\nThe average number of boxes of cookies sold was: {0:.1f}.".format(averageBoxesSold))
        print("\nGuide Name\t\tPrize Won")
        print("\n+-----------------------------------------------------+\n")
        for counter in range(len(guidesNamesList)):
            if numberOfCookiesSold[counter] == max(numberOfCookiesSold):
                guidePrizeAwarded(guidesNamesList, counter, prizeList, 0)
            elif numberOfCookiesSold[counter] > averageBoxesSold:
                guidePrizeAwarded(guidesNamesList, counter, prizeList, 1)
            elif numberOfCookiesSold[counter] >= 1:
                guidePrizeAwarded(guidesNamesList, counter, prizeList, 2)
            else:
                guidePrizeAwarded(guidesNamesList, counter, prizeList, 3)
            print("")

    else:
        print("\nError! You have entered an invalid value. Please try again.")
        main()
    
    #Your code ends on the line above.

#Do not change any of the code below!
if __name__ == "__main__":
    main()