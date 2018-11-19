# 2D lists

my2DList = []

my2DList.append(["A","B","C"])
my2DList.append(["D","E","F"])
my2DList.append(["G","H","I"])

# for row in my2DList:
#     for colmun in row:
#         print(colmun,end=", ")
#     print()

for row in range(len(my2DList)):
    for colmun in range(len(my2DList)):
        print(my2DList[row][colmun])

my3DList = []
my3DList = [[["A","B"],["C","D"]], [["E","F"],["G","H"]]]
print(my3DList)



print(my3DList)


for row in my2DList:
    for colmun in row:
        print(colmun)

# for time in range(len(my3DList)):
#     for row in range(len(my3DList)):
#         for colmun in range(len(my3DList)):
#             print(my3DList[time][row][colmun])

