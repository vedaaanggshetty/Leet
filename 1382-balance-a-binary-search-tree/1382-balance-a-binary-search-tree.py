# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # Inorder traversal
        
        def BT(node):
            if not node:
                return []
            return BT(node.left) +  [node.val] + BT(node.right)


        def BST(nums):
            if not nums:
                return None
            m = len(nums)//2
            root = TreeNode(nums[m])
            root.left = BST(nums[:m])
            root.right = BST(nums[m+1:])
            return root
        
        sorrted = BT(root)
        return BST(sorrted)