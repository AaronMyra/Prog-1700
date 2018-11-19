#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    print("\nWhould you like to restart? ") 
    answer = input("yes or no? ").upper()
    if answer == ("YES"):
        print("\nSucess\n")
        continue
    if answer == "NO":
        print("Ok then\n")
    else: print("Invaild Input\n")
            main()
    



    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()