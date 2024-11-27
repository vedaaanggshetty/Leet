class Solution(object):
    def subarraysDivByK(self, nums, k):
        seen = defaultdict(int)
        seen[0]=1
        currSum = ans = 0

        for num in nums:
            currSum+=num
            rem = currSum%k
            ans+= seen[rem]
            seen[rem]+=1

        return ans
