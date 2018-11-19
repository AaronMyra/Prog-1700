#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Aaron Myra  
Program Title:  Loops With Lists
Description:    Several programs working with loops combined with lists
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    def Program1():

        OddNumbersList = []
        EvenNumberList = []
        SqrNumberList = []
        OddNumberSequenceList = []
        OddNumberSequence = [1,5,4,6,5,8,4,6,8,4]

        for counter in range(0,101,2):
            EvenNumberList.append(counter)
            OddNumbersList.append(counter + 1)
        for counter in range(11):
            SqrNumberList.append(counter * counter)
        for counter in range(len(OddNumberSequence)):
            if (OddNumberSequence[counter] % 2) != 0:
                OddNumberSequenceList.append(OddNumberSequence[counter])

            
        SumOddNumberSequence = sum(OddNumberSequenceList)
        SumOddNumbers = sum(OddNumbersList)    
        SqrNumberList = sum(SqrNumberList)
        SumEvenNumbers = sum(EvenNumberList)
        
        print(SumOddNumberSequence)
        print(SumEvenNumbers)
        print(SqrNumberList)   
        print(SumOddNumbers)

    Program1()


    def Program2():

        s = 0
        while s < 9:
            s = s + 1
        print(s)

    Program2()

    def Program3():

        EvenInputs = []
        Oddinputs = []
        NumberList = []
        CumulativeNumbers = []
        AdjcentNumbers = []

        for counter in range(10):
            NumberList.append(int(input("Enter number {0}: ".format(counter + 1))))
            if (NumberList[counter] % 2) == 0:
                EvenInputs.append(NumberList[counter])
            else:
                Oddinputs.append(NumberList[counter])
            if counter >= 1:
                CumulativeNumbers.append(sum(NumberList))
                if NumberList[counter] == NumberList[counter - 1]:
                    AdjcentNumbers.append(NumberList[counter])
            else:
                CumulativeNumbers.append(NumberList[counter])
            
        print("Largest number: {0}.".format(min(NumberList)))
        print("Smallest number: {0}.".format(max(NumberList)))
        print("Even Numbers: {0}".format(EvenInputs))
        print("Odd Numbers: {0}".format(Oddinputs))
        print("Cumulative Numbers: {0}.".format(CumulativeNumbers))
        print("Adjcent numbers: {0}.".format(AdjcentNumbers))
        
    Program3()

    def Program4():

        UserInput = []

        for counter in range(5):
            UserInput.append(int(input("Enter number {0}: ".format(counter + 1))))

        print("Average user input: {0}.".format(sum(UserInput) / 5))
        print("Minimum user input: {0}.".format(min(UserInput)))
        print("Maximum user input: {0}.".format(max(UserInput)))
        print("Range of user input: {0}.".format(len(UserInput)))

    Program4()

    def Program5():

        UserName = input("Enter your Name: ")

        UserNamelist = list(UserName)
        for counter in range(len(UserNamelist)):
            print(UserNamelist[counter])

    Program5()

    def Program6():

        import random

        RandomNumberList = []
        EvenRandomNumbers = []
        EvenIndexNumbers =[]

        for counter in range(10):
            RandomNumberList.append(random.randint(1, 21))
            if RandomNumberList[counter] % 2 == 0:
                EvenRandomNumbers.append(RandomNumberList[counter])

        print("Random numbers: {0}.".format(RandomNumberList))

        for counter in range(0, 10, 2):
            EvenIndexNumbers.append(RandomNumberList[counter])

        print("Numbers at even indexes: {0}.".format(EvenIndexNumbers))
        print("First number: {0}.".format(RandomNumberList[0]))
        print("Last number: {0}.".format(RandomNumberList[-1]))
        RandomNumberList.reverse()
        print("Random numbers reversed: {0}.".format(RandomNumberList))
        print("Even random numbers: {0}.".format(EvenRandomNumbers))

    Program6()





    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()