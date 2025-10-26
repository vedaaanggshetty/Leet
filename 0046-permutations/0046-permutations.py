class Solution(object):
    def permute(self, nums):
        res = []

        def BT(p, seen):
            if len(p) == len(nums):
                res.append(p[:])
                return 

            for i in range(len(nums)):
                if i not in seen:
                    seen.add(i)
                    p.append(nums[i])
                    BT(p, seen)
                    p.pop()
                    seen.remove(i)
            
        BT([], set())
        return res