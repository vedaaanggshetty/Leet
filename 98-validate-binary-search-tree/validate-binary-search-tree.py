# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def BT(node, l, h):
            if not node:
                return True
            if not (l < node.val < h):
                return False

            return (BT(node.left, l, node.val) and BT(node.right, node.val, h))

        return BT(root, float('-inf') , float('inf'))
        