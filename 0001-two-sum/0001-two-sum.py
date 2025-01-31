class Solution(object):
    def twoSum(self, nums, target):
        # # ill do binary search here
        # nums.sort()
        # l = 0
        # r = len(nums)-1
        # print(nums)
        # while l < r:
        #     tot = nums[l] + nums[r]

        #     if(tot == target):
        #         return [l+1, r+1]
        #     elif tot < target:
        #         l += 1
        #     else:
        #         r -= 1
        # return []
        hashM = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashM:
                return [i, hashM[diff]]
            hashM[n] = i
        return hashM