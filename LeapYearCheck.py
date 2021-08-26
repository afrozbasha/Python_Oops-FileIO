"""
    @Author: Afroz Basha
    @Date: 2021-08-23
    @Title: Replace String Template
"""


def checkYear(year):
    """ Checking the Leap Year"""
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
n = int(input("Enter a year 4 digits must : "))
checkYear(n)
