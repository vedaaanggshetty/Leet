class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        if sum(nums) % k != 0:
            return False
        total = sum(nums) // k
        visit = [False] * len(nums)
        nums.sort(reverse=True)

        def BT(i, k, subSum):
            if k == 0:
                return True
            if subSum == total:
                return BT(0, k-1, 0)

            for j in range(i, len(nums)):
                if visit[j] or subSum + nums[j] > total:
                    continue
                visit[j] = True
                if BT(j+1, k, subSum + nums[j]):
                    return True
                visit[j] = False

                if subSum == 0: break

            return False

        return BT(0, k, 0)
