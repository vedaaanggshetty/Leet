# from functools import cmp_to_key

class Solution(object):
     def largestNumber(self, nums):
        for i,n in enumerate(nums):
            nums[i] = str(n)  # nums[0] = 10 = "10"
        
        def compare(n1,n2):
            if(n1+n2 > n2 + n1): # if 34+5 > 5+34 then let n2 first
                return -1
            else:
                return 1
        nums = sorted(nums, key = cmp_to_key(compare))  #[9,5,32,3]
    
        return "".join(nums)


    