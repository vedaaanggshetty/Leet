class Solution(object):
    def maxScore(self, nums1, nums2, k):
        maxScore = float('-inf')
        # help(zip)
        comb = sorted(zip(nums2, nums1), reverse= True)
        l = []
        summ = 0

        for n2,n1 in comb:
            heapq.heappush(l, n1)
            summ += n1

            if len(l) > k:
                summ -= heapq.heappop(l)
       
            if len(l) == k:
                maxScore = max(maxScore, n2 * summ)
        
        return maxScore