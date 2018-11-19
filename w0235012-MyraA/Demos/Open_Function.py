#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    Writing Data to Files Demo
"""

def main():

    # Open Function
    # myFile = open(fileName, accessMode)
    # fileName can be EX. data.txt, myTimes.csv
    # Open file object - if file doen't exist it will create it

    fileName2 = "AaronFile.txt"
    accessMode2 = "w"
    myFile = open(fileName2, accessMode2)

    #Write a value into the file
    myFile.write("We are the Champions\n")
    myFile.write("... of the world!")


    #Close my file - When opening a file always close file when done
    myFile.close()
    


if __name__ == "__main__":
    main()