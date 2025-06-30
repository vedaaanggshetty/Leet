# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        minn = float('inf')
        prev = float('-inf')
        s = []
        while s or root:
            if root:
                s.append(root)
                root = root.left
            else:
                root = s.pop()
                minn = min(minn, root.val - prev)
                prev = root.val
                root = root.right   
        return minn