"""
    @Author: Afroz Basha
    @Date: 2021-08-25
    @Title: 2D ARRAY
"""
import random

"""
Description:
   Given N distinct Coupon Numbers, how many random numbers do you need to generate distinct coupon number? This program simulates this random process. 

Parameter:
    N Distinct Coupon Number with class in static method

Return:
   total random number needed to have all distinct numbers
"""

num = int(input("Enter the Total no of coupons Num : "))


class CouponNum(object):
    @staticmethod
    def couponNumGen(num):
        dist, count = 1, 0
        clot = []

        while dist <= num:
            value = random.randrange(num)
            count += 1
            print("Generated value ", value + 1)
            for i in range(len(clot)):
                if clot[i] != value:
                    dist += 1
                    if dist == num:
                        break
                    clot.append(value)

        print("Total no of trials to get ", num, " different coupon number's are ", count)
        print(" ")
        print("List : ")
        for i in range(num):
            print(i, "elements in the list is ", clot[i])
        pass


x = CouponNum()
x.couponNumGen(num)
