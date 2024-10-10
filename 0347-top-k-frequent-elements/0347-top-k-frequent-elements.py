from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        freq_map = Counter(nums)  # Hash[3,2,1]
        buckets = [[] for _ in range(len(nums) + 1)] # buckets = [[] , [], [], []]

        for num, freq in freq_map.items():
            buckets[freq].append(num)  # buckets[3].append(1) = buckets = [[],[],[],[3],[]]

        res = []
        for i in range(len(buckets)-1,0,-1): # backward loop
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

#      #	Step 1: The frequency map is {1: 3, 2: 2, 3: 1}.
# Step 2: The buckets list would look like this:
# buckets = [[], [3], [2], [1], [], []]
# Step 3: Starting from the right (i.e., buckets[3]), we add the element 1 (which appears 3 times), and then move to buckets[2] and add the element 2 (which appears 2 times).
# Step 4: The result will be [1, 2].
#    
