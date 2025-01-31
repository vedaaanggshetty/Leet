# import Counter
class Solution(object):
    def majorityElement(self, nums):
        # import counter
        res =[]
        n = len(nums)
        freq = Counter(nums)
        # you can enumerate using dict
        for k,v in freq.items():
            if v > n/3:
                res.append(k)
        return res