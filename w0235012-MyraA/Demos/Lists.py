#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    # elements = ["copper","helium","argon","magnesium"]
    # print(elements)
    
    # #remove list item 
    # elements.remove("copper")
    # print(elements)

    # #or - del elements[0]

    # #add list items
    # elements.append("copper")
    # # print(elements)

    # # #list counts
    # # print(len(elements))
    # # print(min(elements))
    # # print(max(elements))

    # # #sort list
    # # elements.sort()
    # # print(elements)

    # # daysOfTheWeek = ["Sunday", "Monday"]
    # # grades = ["A", "B", "C", "D", "F"]

    # #make a list of animals
    # animals = []

    # #method 1
    # animals1 = input("Enter the name of an animal: ")
    # animals.append(animals1)

    # #Method 2
    # animals.append(input("Enter the name of an animal: "))

    # #Method 3
    # for counter in range(2):
    #     animals.append(input("Enter the name of animal {0}: ".format(counter + 1)))

    # numberOfAnimals = len(animals)
    # animals.sort()
    # animals.reverse()

    # for counter in range(len(animals)):
        
    #     print(animals[counter])

    # Hook up a loop to a list directly

    cheeses = ["gouda", "chessies", "cheddar", "mozzaarella", \
                "Amurcn", "Asiago", "Edam", "Gorgonzolla"]

    for counter in range(len(cheeses)):
        print("I want to eat {0} cheese.\n".format(cheeses[counter]))



    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()