class Solution(object):
    def maxFrequency(self, nums, k):
        n = len(nums)
        nums.sort()
        summ = 0
        l = 0
        res = 0
        for r in range(n):
            summ += nums[r]

            while (nums[r] * ( r - l + 1) - summ) > k:
                summ -= nums[l]
                l += 1

            res = max(res, r - l + 1)
        return res




    
        # freq = Counter(nums)
        # maxx = nums[0]
        # c = 0


        # for key, val in freq.items():
        #     if key > maxx:
        #         maxx = key
                
            
        #     if val == k:
        #         return c

        #     elif key < k:
        #         k -= key

    