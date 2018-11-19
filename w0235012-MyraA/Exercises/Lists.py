#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Aaron Myra
Program Title:  List
Description:    Several programs that work with lists
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    def FirstOrLast7(ChangeToMax):
        numbersList = ChangeToMax
        if ChangeToMax[0] == 7 or ChangeToMax[-1] == 7:
            print("True")
        else:
            print("False")


    FirstOrLast7([13,7,1,5,9])

    def ReverseNumbers(ChangeToMax):

        ReverseIt = ChangeToMax
        ReverseIt.sort()
        ReverseIt.reverse()
    
        print(*ReverseIt)

    ReverseNumbers([1, 2, 3])

    def Elements(ChangeToMax1, ChangeToMax2):
        
        MiddleElements = []
        MiddleElements.append(ChangeToMax1[1])
        MiddleElements.append(ChangeToMax2[1])
        print(*MiddleElements)

    Elements([7, 7, 7], [3, 8, 0])

    def SumNumbers(ChangeToMax):
        
        SumList = ChangeToMax[0] + ChangeToMax[1] + ChangeToMax[2]
        print(SumList)
        
    SumNumbers([5, 11, 2])

    def MaxNumbers(ChangeToMax):

        if ChangeToMax[0] > ChangeToMax[2]:
            ChangeToMax[1] = ChangeToMax[0]
            ChangeToMax[2] = ChangeToMax[0]
        else:
            ChangeToMax[0] = ChangeToMax[2]
            ChangeToMax[1] = ChangeToMax[2]

        print(*ChangeToMax)

    MaxNumbers([11, 22, 3])

    def RotateNumbers(RotateLeft):
        RotateLeft.append(0)
        RotateLeft[3] = RotateLeft[0]
     
        RotateLeft.remove(RotateLeft[0])


        print(*RotateLeft)

    RotateNumbers([1, 2, 3])

    def TrueNumbers(p_Has2Or3):

        if 2 in p_Has2Or3 or 3 in p_Has2Or3:
            print("True")

        else:
            print("False")

    TrueNumbers([5,5])




    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()