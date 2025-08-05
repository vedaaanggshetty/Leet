class Solution:
    def canJump(self, nums: List[int]) -> bool:
        x = 0
        for i , v in enumerate(nums):
            if i > x:
                return False
            x = max(x, i + v)
        return True