"""
    @Author: Afroz Basha
    @Date: 2021-08-23
    @Title: Replace String Template
"""

def PowerOfNym(n):
    """ Checking the Leap Year by taking the 2 range multiplication number """
    pow = 1;
    for i in range(n):
        if i == 31: break
        pow *= 2 ** 1
        print("2 power of " + str(i) + "is : " + str(pow))
    year = pow
    try:
        if year % 400 == 0:
            print(str(year) + "is a leap year")
        elif year % 100 == 0:
            print(str(year) + "is not a leap year")
        elif year % 4 == 0:
            print(str(year) + "is a leap year")
        else:
            raise Exception
    except Exception:
        print(str(year) + "is not a leap year")


# taking input passing methods
n = int(input("Enter a digits : "))
PowerOfNym(n)
