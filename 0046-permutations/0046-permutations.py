class Solution(object):
    def permute(self, nums):
        res = []

        def BT(p, arr):
            if len(p) == len(nums):
                res.append(p[:])
                return

            for i in range(len(nums)):
                if not arr[i]:
                    arr[i] = True
                    p.append(nums[i])
                    BT(p, arr)           
                    p.pop()
                    arr[i] = False

        BT([], [False] * len(nums))
        return res