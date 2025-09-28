class Solution(object):
    import random
    def getNoZeroIntegers(self, n):
        def zero(i):
            return '0' not in str(i)

        for a in range(1,n):
            b = n - a
            if zero(a) and zero(b):
                return [a,b]