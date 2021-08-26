"""
    @Author: Afroz Basha
    @Date: 2021-08-24
    @Title: Quadratic Equation
"""
import math

"""
Description:
    Using Math Function 
Parameter:
    delta = b*b - 4*a*c
    Root 1 of x = (-b + sqrt(delta)) / (2*a)
    Root 2 of x = (-b - sqrt(delta)) / (2*a)
Return:
      It returns the real and imaginary root
"""

a = int(input("Enter the value of A : "))

b = int(input("Enter the value of B : "))

c = int(input("Enter the value of C : "))

try:
    """find the roots of the equation a*x*x+b*x+c"""
    if a != 0:
        delta = b * b - 4.0 * a * c
        if delta > 0:
            r1 = float((-b + math.sqrt(delta)) / (2 * a))
            r2 = float((-b - math.sqrt(delta)) / (2 * a))
            print("Root1 : %.2f", r1, "Root2 : %.2f", r2)
        elif delta ==0:
            r1 = r2 = -b / (2 * a)
            print("Root1 : Root2 : ", r1)
        else:
            real = float(-b / (2 * a))
            imaginary = float(math.sqrt(-delta) / (2 * a))
            print("Root1 : ", real, " + ", imaginary, " i")
            print()
            print("Root2 : ", real, " + ", imaginary, " i")
except ValueError:
    print("Enter a Numeric value")
except ZeroDivisionError:
    print("Division by Zero Error")