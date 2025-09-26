# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)

        elif root.val > key:
            root.left  = self.deleteNode(root.left, key)

        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

        
            s = self.find(root.right)
            root.val = s.val
            root.right = self.deleteNode(root.right, s.val)
        return root

    def find(self, node):
        while node.left:
            node = node.left

        return node