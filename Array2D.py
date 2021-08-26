"""
    @Author: Afroz Basha
    @Date: 2021-08-24
    @Title: 2D ARRAY
"""

"""
Description:
   A library for reading the input in 2D arrays and printing them out to standard output.
Parameter:
   rowSize rows, colSize Cols, and rowSize * colSize inputs for 2D Array.
Return:
      Print function to print 2 Dimensional Array.
"""

rowSize = int(input("Enter the number of rows: "))
colSize = int(input("Enter the number of columns: "))


def createMatrix(rowSize, colSize):
    """Print function to print 2 Dimensional Array"""
    array2D = []
    print("Enter the elements : ")
    for i in range(rowSize):
        array = []
        for j in range(colSize):
            array.append(int(input()))
        array2D.append(array)
    print("The 2D array is given below:")
    for i in range(rowSize):
        for j in range(colSize):
            print(str(array2D[i][j]), end=" ")
        print()
    pass


createMatrix(rowSize, colSize)
