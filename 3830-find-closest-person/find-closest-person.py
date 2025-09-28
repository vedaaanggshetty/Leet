class Solution(object):
    def findClosest(self, x, y, z):
        if abs(x-z) == abs(y-z):
            return 0        
        return 2 if abs(x-z) > abs(y-z) else 1

            