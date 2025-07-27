class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        cons = 0
        for i in nums:
            if i == 1:
                count += 1
                cons = max(cons,count)        
            if i == 0:
                count = 0
        return cons