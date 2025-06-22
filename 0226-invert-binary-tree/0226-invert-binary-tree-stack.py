# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        # if root:
        #     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root

        # Stack
        s = [root]
        while s:
            n = s.pop()
            if n:
                n.left, n.right = n.right, n.left
                s.extend([n.right, n.left])        
        return root
