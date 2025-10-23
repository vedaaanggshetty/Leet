class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        a = numBottles
        e = numBottles
        x = numExchange
        while x <= e:
            e -= x
            a += 1
            x += 1
            e += 1
        return a



        