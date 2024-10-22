class Solution(object):
    def missingInteger(self, nums):
        # TAKE ONE
        # nums.sort()
        # summ = 0
        # for s in nums:
        #     summ += s
        # n = len(nums)
        # otherSum = n * (n+1)/2 + n/2
        # total = 0
        # total = otherSum - summ
        # return total
        

        # TAKE TWO
        # nums.sort()
        # curr = 0
        # maxSum = float('-inf')
        # for num in nums:
        #     curr += num
        #     if curr > maxSum:
        #         maxSum = curr       
        
        # return maxSum

        n = len(nums)
        seq = nums[0]
        last = 0

        for i in range(1,n):
            if nums[i] == nums[i-1] + 1: # 2 = 1 + 1
                seq += nums[i] # 1 += 2 => 3
                last  = i # last = 1
            else:
                break
        

        missing = seq
        numSet = set(nums)

        while missing in numSet:
            missing += 1
        
        return missing
           
          
        
