class Solution(object):
    def continuousSubarrays(self, nums):
        res = []
        n = len(nums)
        l = 0
        ans = 0

        maxx = deque()
        minn = deque()

        for r in range(n):
            while maxx and nums[maxx[-1]] < nums[r]:
                maxx.pop()
            maxx.append(r)

            while minn and nums[minn[-1]] > nums[r]:
                minn.pop()
            minn.append(r)

            while nums[maxx[0]] - nums[minn[0]] > 2:
                l += 1
                if maxx[0] < l:
                    maxx.popleft()
                if minn[0] < l:
                    minn.popleft()

            ans += ( r - l + 1)
        return ans