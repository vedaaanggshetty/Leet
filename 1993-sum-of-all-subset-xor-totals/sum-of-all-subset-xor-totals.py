class Solution(object):
    def subsetXORSum(self, nums):
        xor = [0] 

        def BT(n, arr):
            
            if n == len(nums):
                xor[0] += arr
                return

            # choice 1: don't include current element
            BT(n + 1, arr)

            # choice 2: include current element (use n instead of undefined i)
            BT(n + 1, arr ^ nums[n])

        BT(0, 0)
        return xor[0]
