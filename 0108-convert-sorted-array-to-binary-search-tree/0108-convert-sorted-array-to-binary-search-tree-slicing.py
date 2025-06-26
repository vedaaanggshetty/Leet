# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        # RECURSIVE

        def BT(l, r):
            if l > r:
                return None
            
            m = (l + r)//2
            node = TreeNode(nums[m])

            node.left = BT(l, m-1)
            node.right = BT(m+1, r)

            return node
        
        return BT(0, len(nums)-1)