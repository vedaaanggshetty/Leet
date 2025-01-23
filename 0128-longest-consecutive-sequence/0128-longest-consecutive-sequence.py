class Solution(object):
    def longestConsecutive(self, nums):
        # count = 0
        # sortedNums = sorted(nums)
        # # print(sortedNums)
        # for i in range(len(nums)-1):
        #     if (nums[i+1] == nums[i]+1):
        #         count += 1
        # return count
        longg = 0
        numS = set(nums)
        # {100,4,200,1,3,2}
        for n in numS:
            if n-1 not in numS:
                currN = n
                currStreak = 1

                while currN + 1 in numS:
                    currN += 1
                    currStreak +=1
                longg = max(currStreak, longg)
        return longg
