class Solution(object):
    def checkSubarraySum(self, nums, k):
        # O(N3)
        # n = len(nums)
        # summ = 0
        # if len(nums) == k:
        #     return False
        # for i in range(n):
        #     for j in range(i,n):
        #         sub = nums[i:j+1]
        #         summ = sum(sub)
        #         if summ % k == 0:
        #             return True
        # return False

        # O(N2)

        # n = len(nums)
        # pre = [0] * (n+1)

        # for i in range(n):
        #     pre[i+1] = pre[i] + nums[i]
        # for i in range(n):
        #     for j in range(i+1, n):
        #         summ = pre[j+1] - pre[i]
        #         if summ % k == 0:
        #             return True
        # return False
        
        n = len(nums)
        p = 0
        sett = {0:-1}
        for i, num in enumerate(nums):
            p += num

            if k != 0:
                p %= k

            if p not in sett:
                sett[p] = i
            elif p in sett:
                if i - sett[p] > 1:
                    return True
        return False