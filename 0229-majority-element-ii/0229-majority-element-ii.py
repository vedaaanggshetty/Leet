# import Counter
class Solution(object):
    def majorityElement(self, nums):
        # # import counter
        # res =[]
        # n = len(nums)
        # freq = Counter(nums)
        # # you can enumerate using dict
        # for k,v in freq.items():
        #     if v > n/3:
        #         res.append(k)
        # return res

    # ------------  better efficiency ----------
        res = []
        n = len(nums)
        freq = n // 3
        for i in set(nums):
            if (nums.count(i) > freq):
                res.append(i)
        return res