class Solution(object):
    def threeSum(self, nums):
        target = 0
        sset = set()
        nums.sort()
        n = len(nums)
        i = 0
        res = []
        for i in range(n):
            j, k = i+1, n-1
            while j<k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    sset.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    k -= 1
        res = list(sset)
        return res

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        # res = []
        # i = 0
        # j = 1
        # k = 2
        # while(i!=j and i!=k and j != k):
        #     for n in nums:
        #         if (nums[i] + nums[j] + nums[k] == 0):
        #             res.append(nums[1:3])
        #         else:
        #             res.append(0)
        # return res
        