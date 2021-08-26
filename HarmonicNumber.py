"""
    @Author: Afroz Basha
    @Date: 2021-08-23
    @Title: Replace String Template
"""


def harmonicNum(n):
    """Prints the Nth harmonic number"""
    sum = 0
    for i in range(1, n + 1):
        sum += 1 / i
        if i == 1:
            print("1 + ")
        else:
            print("1/" + str(i))
    print("\n")
    print("Sum of the series is : " + str(sum))


# taking input passing methods
n = int(input("Enter a digits : "))
if n <= 0:
    print("Please enter the num greater than zero")
harmonicNum(n)
