#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Aaron 
Program Title:  Practice_Exercise_2
Description:    RICK_ROLLED
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    print("Hello, Welcome To The Song Generator!")
    name = input("Please Enter a Name: ")
    phrase = input("Please Enter a Short Word Phrase: ")
    print("""Never gonna give you up
Never gonna let you down, """ + name)
    print("Never gonna run around and desert you\nNever gonna make "\
    + name + " cry")
    print("Never gonna say '{0}'".format(phrase))
    print("Never gonna tell a lie and hurt you")

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()