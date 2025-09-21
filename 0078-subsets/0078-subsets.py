class Solution(object):
    def subsets(self, nums):
        res = []

        def BT(i, sub):
            if i == len(nums):
                res.append(list(sub))
                return 

            BT(i+1, sub)

            sub.append(nums[i])
            BT(i+1, sub) 
            sub.pop()



        BT(0, [])
        return res
