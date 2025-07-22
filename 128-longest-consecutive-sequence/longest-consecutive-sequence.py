class Solution(object):
    def longestConsecutive(self, nums):
        cons = 0
        numS = set(nums)
        print(numS)
        for n in numS:
            if n - 1 not in numS:
                length = 1

                while length + n in numS:
                    length += 1    
                cons = max(cons, length)

        return cons