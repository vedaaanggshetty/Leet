class Solution(object):
    def findClosest(self, x, y, z):
        if abs(x-z) == abs(y-z):
            return 0
        elif abs(x-z) > abs(y-z):
            return 2
        else:
            return 1
        
        # return 2 if abs(x-z) > abs(y-z) else 1

        