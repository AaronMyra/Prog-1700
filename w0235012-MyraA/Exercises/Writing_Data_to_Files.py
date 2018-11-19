#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""

def main(): 
    
    fileName = "nameAndAgeData.csv"
    accessMode = "w"
    guestName = []
    guestAge = []

    myFile = open(fileName, accessMode)
    for counter in range(int(input("\nEnter the number of guests: "))):
        guestName.append(input("Enter the name of guest {0}: ".format(counter + 1)).capitalize())
        if guestName[counter].isalpha():
            guestAge.append(input("Enter the age of {0}: ".format(guestName[counter])))
            myFile.write(guestName[counter] + ", " + guestAge[counter]  + "\n")

        else:
            while not guestName.isalpha():
                print("\nError! You have entered an invalid name. Please try again.\n")
                guestName[counter].append(input("Enter the name of guest {0}: ".format(counter + 1)).capitalize())
            guestAge.append(input("Enter the age of {0}: ".format(guestName[counter])))
            myFile.write(guestName[counter]  + ", " + guestAge[counter]  + "\n")

    print("\nGuest list complete!\n")
    for counter in range(len(guestName)):
        print("Name: " + guestName[counter])
        print("Age: " + guestAge[counter] + "\n")
    
    myFile.close()

   


if __name__ == "__main__":
    main()