"""
    @Author: Afroz Basha
    @Date: 2021-08-23
    @Title: Replace String Template
"""


def PrimeFact(num):
    """ Number to find the prime factors """
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)


# taking input passing methods
n = int(input("Enter a digits : "))
if n <= 0:
    print("Please enter the num greater than zero")
else:
    PrimeFact(n)
