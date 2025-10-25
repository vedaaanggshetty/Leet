class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        

    def sumRange(self, left, right):
        res = []
        summ = 0
        for j in range(left, right+1):
            summ += self.nums[j]
        return summ


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)