"""
    @Author: Afroz Basha
    @Date: 2021-08-24
    @Title: Euclidean distance from the point (x, y) to the origin (0, 0)
"""
import math

"""
Description:
    Using Math Function 
Parameter:
     distance from the point (x,y) to the origin (0,0).
Return:
      List of variable values are X and Y to find the distance using given formula 
"""

x = int(input("Enter the x co-ordinate of the first point: "))
y = int(input("Enter the y co-ordinate of the first point: "))


def distances(x, y):
    """calculate distance = sqrt(x*x + y*y)"""
    dis = math.sqrt((x ** 2 + y ** 2))
    print(dis)
    pass


distances(x, y)
