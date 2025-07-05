# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        def dfs(node, maxx):
            if not node:
                return 0
            c = 1 if node.val >= maxx else 0 
            maxx = max(maxx, node.val)           
            c += dfs(node.left, maxx)
            c += dfs(node.right, maxx)

            return c
        return dfs(root, root.val)