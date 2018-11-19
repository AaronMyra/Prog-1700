#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Aaron Myra 
Program Title:  Practice
Description:    String Manipulation
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    phrase=input("Please Enter a Phrase: ")
    print("You Entered :" + phrase)
    print("That phrase in uppercase is: " + phrase.upper())
    print("That phrase in lowercase is: " + phrase.lower())
    print("There are {0}".format(phrase.count("o")) + " o's in the phrase")
    print("Does the phrase contain only alpha-numeric characters? ")\
    print(phrase.isalnum())
    print("Replacing the s's with z's in the phrase would look like this: ")
    print(phrase.replace("s","z"))
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()