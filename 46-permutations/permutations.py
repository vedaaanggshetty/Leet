class Solution(object):
    def permute(self, nums):
        def BT(s, e):
            if s == e:
                res.append(nums[:])
                return
            for i in range(s,e):
                nums[s], nums[i] = nums[i], nums[s]
                BT(s+1, e)
                nums[s], nums[i] = nums[i], nums[s]
        res = []
        BT(0, len(nums))
        return res
