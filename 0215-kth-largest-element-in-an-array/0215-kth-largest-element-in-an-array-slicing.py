class Solution(object):
    def findKthLargest(self, nums, k):
        sortNums = sorted(nums)
        size = 0
        # numSet = {}
        size = sortNums[-k]
        # for i in sortNums:
        #     if i not in sortNums:
        #         numSet.append(i)
        
        return size