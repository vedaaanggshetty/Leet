class Solution(object):
    def findDisappearedNumbers(self, nums):
        res = []
        numset = set(nums)
        # sorted(numset)
        # print(numset)
        for i in range(1, len(nums)+1):
            if i not in numset:
                res.append(i)
        return res