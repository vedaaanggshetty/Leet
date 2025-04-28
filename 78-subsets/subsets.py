class Solution(object):
    def subsets(self, nums):
        res = []
        sub = []
        def BT(i):
            if i >= len(nums):
                # res.append(sub.copy())
                res.append(sub[:])
                return 
            
            sub.append(nums[i])
            BT(i+1)
            
            sub.pop()
            BT(i+1)
        BT(0)
        return res