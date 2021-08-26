"""
    @Author: Afroz Basha
    @Date: 2021-08-24
    @Title: Sum of three Integer adds to zero
"""

"""
Description:
   A program with cubic running time. Read in N integers and counts the number of triples that sum to exactly 0.
Parameter:
    Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
Return:
      List of variable values are i , j , k
"""

n = int(input("Enter Nums range n : "))
arrayList = []

print("Enter int elements of the list : ")
for i in range(n):
    arrayList.append(int(input()))


def threeIntZero(n, arrayList):
    """Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0"""
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arrayList[i] + arrayList[j] + arrayList[k] == 0:
                    print(arrayList[i], arrayList[j], arrayList[k])
    pass


threeIntZero(n, arrayList)