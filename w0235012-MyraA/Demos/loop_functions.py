#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    for rocketCountdown in range(60, -1, -1):
        print(rocketCountdown)
        if rocketCountdown == 0:
            print("\nBLAST OFF!")

    
    personName = ""

    while personName != "Done":
        personName = input("\nEnter a name or enter 'Done' to exit: ").capitalize()
        if personName != "Done":
            print("\nGood Morning " + personName)
    
    
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()