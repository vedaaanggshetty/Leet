from math import floor
from math import ceil
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """ 
        q =  ( abs(dividend) / abs(divisor) )
        if ((dividend) < 0) ^ ((divisor) < 0):
            q = -q 
        minn = -2 ** 31
        maxx = 2 ** 31 -1 
        
        return max(min(q, maxx),minn)