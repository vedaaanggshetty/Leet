from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        freq_map = Counter(nums)  # Hash[3,2,1]
        buckets = [[] for _ in range(len(nums) + 1)] # buckets = [[] , [], [], []]

        for freq, num in freq_map.items():
            buckets[freq].append(num)  # buckets[3].append(1) = buckets = [[],[],[],[3],[]]

        res = []
        for i in range(len(buckets)-1,0,-1): # backward loop
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        