"""
    @Author: Afroz Basha
    @Date: 2021-08-25
    @Title: 2D ARRAY
"""
import random
import sys

"""
Description:
 Simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
times he/she wins and the number of bets he/she makes. Run the experiment N
times, averages the results, and prints them out.

Parameter:
    No Syntax only Logic Using While and if condition
    
Return:
        It returns the amount gambled.
"""


class Gambler(object):
    def __init__(self, rs, lossc, win, count, winc):
        self.Rs = rs
        self.lossCount = lossc
        self.win = win
        self.winCount = winc
        self.count = count

    def gamblerPlaying(self):
        while True:
            bet = random.randrange(2)
            self.count += 1
            if bet == 1:
                self.Rs += 1
                self.winCount += 1
                if self.Rs == self.win:
                    print("You win 100 Rs")
                    print("You win ", self.winCount, " times")
                    print("You attempted ", self.count, " times")
                    sys.exit()
            else:
                self.Rs -= 1
                self.lossCount += 1
                if self.Rs == 0:
                    print("You loss 100 Rs")
                    print("You loss ", self.lossCount, " times")
                    print("You attempted ", self.count, " times")
                    sys.exit()


x = Gambler(100, 0, 200, 1, 0)
x.gamblerPlaying()
