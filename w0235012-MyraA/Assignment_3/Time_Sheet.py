#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Aaron Myra
Program Title:  Time Sheet
Description:    Determines which days the user worked the most, the user worked less than 7 hours, 
                total hours worked and the daily average the user worked
"""

# Functions
# Calculate days with most hours worked
def maxHoursWorked(mostHoursWorked, p_userHoursWorked, p_counter):
    if p_userHoursWorked[p_counter] == max(p_userHoursWorked):
        mostHoursWorked.append(p_userHoursWorked[p_counter])
        mostHoursWorked.append(p_counter + 1)
    return mostHoursWorked

# Which days did the user work less than normal hours
def insufficientHoursWorked(insufficientHours, p_userHoursWorked, p_normalHoursWorked, p_counter):
    if p_userHoursWorked[p_counter] < p_normalHoursWorked:
        insufficientHours.append(p_counter + 1)
        insufficientHours.append(p_userHoursWorked[p_counter])
    return insufficientHours

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    print("\nWelcome to the Time Sheet Program.")

    # Initializing variables
    userHoursWorked = []
    mostHoursWorked = []
    totalHoursWorked = 0
    insufficientHours = []
    normalHoursWorked = 7

    # User input for hours for each day
    for counter in range(5):
        userInput = input("\nEnter the number of hours worked on day #{0}: ".format(counter + 1))
        if userInput.isnumeric():
            userHoursWorked.append(float(userInput))

        else:
            while not userInput.isnumeric():
                print("ERROR! You have entered an invalid value. Please try again\n")
                userInput = input("\nEnter the number of hours worked on day #{0}: ".format(counter + 1))
                if userInput.isnumeric():
                    userHoursWorked.append(float(userInput))

    # If there is more than one day with the most hours
    for counter in range(len(userHoursWorked)):
        
        # Calculate the total hours worked
        totalHoursWorked = totalHoursWorked + userHoursWorked[counter]

        # Use functions calls to calculate days with most and inifficient hours worked
        maxHoursWorked(mostHoursWorked, userHoursWorked, counter)
        insufficientHoursWorked(insufficientHours, userHoursWorked, normalHoursWorked, counter)

    # Average of the total hours worked
    AverageHoursWorked = totalHoursWorked / len(userHoursWorked)

    # Output the data
    print("\n+--------------------------------------------------+")
    print("\nYou worked an inifficient amount of hours (Less than 7 hours) on:\n")
    for counter in range(0, len(insufficientHours), 2):
        print("\tDay #{0} with {1} hours".format(insufficientHours[counter], insufficientHours[counter + 1]))
    if len(insufficientHours) == 0:
        print("\nNo inificient hours worked.") 
    print("\n+--------------------------------------------------+") 
    print("\nYour total hours worked this week is {0:.2f} with a daily average of {1:.2f}.\n".format(totalHoursWorked, AverageHoursWorked))
    print("+--------------------------------------------------+\n") 
    print("You worked the most hours on: \n")
    for counter in range(0, len(mostHoursWorked), 2):
        print("\tDay #{1} with {0} hours".format(mostHoursWorked[counter], mostHoursWorked[counter + 1]))
    print("\n+--------------------------------------------------+\n")

    #Your code ends on the line above.

#Do not change any of the code below!
if __name__ == "__main__":
    main()