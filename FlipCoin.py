"""
    @Author: Afroz Basha
    @Date: 2021-08-23
    @Title: Replace String Template
"""
import random


class tossCoin(object):
    tossHeads, tossTails = 0, 0

    def tossTheCoin(self, n):
        """count the heads, tails and pass to function to findPercentage"""
        try:
            if n >= 0:
                tossHeads, tossTails = 0, 0
                temp = n
                while temp > 0:
                    flipCoin = random.randrange(2)
                    if flipCoin == 0:
                        tossTails += 1
                        print("Tails")
                    else:
                        tossHeads += 1
                        print("Heads")
                    temp = temp - 1
                print("Heads: " + str(tossHeads), "\nTails: " + str(tossTails))
                calculate.findPercentage(n, tossHeads, tossTails)
            else:
                raise IOError
        except IOError:
            print("!Ensure enter the positive integer only")


class calculate(tossCoin):
    """Flip Coin and print percentage of Heads and Tails"""

    def findPercentage(n, tossHeads, tossTails):
        headsPercentage = tossHeads / n * 100
        tailsPercentage = tossTails / n * 100
        print("Percentage of Heads vs Tails")
        print("Percentage of Heads : " + str(headsPercentage))
        print("Percentage of Tails : " + str(tailsPercentage))
        pass


# taking input passing methods via class
n = int(input("Enter the number of times to flip coin: "))
tossCoin().tossTheCoin(n)
