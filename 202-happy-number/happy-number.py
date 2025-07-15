class Solution(object):
    def isHappy(self, n):
        while n != 1:
            digit = [int(d) for d in str(n)]
            sqr = [d ** 2 for d in digit]
            happy = sum(sqr)

            if happy == 1:
                return True
            elif happy == 4:
                return False
            
            n = happy

        return True