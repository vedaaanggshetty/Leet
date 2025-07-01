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
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        def build_balanced_bst(vals):
            if not vals:
                return None
            mid = len(vals) // 2
            node = TreeNode(vals[mid])
            node.left = build_balanced_bst(vals[:mid])
            node.right = build_balanced_bst(vals[mid+1:])
            return node

        sorted_vals = inorder(root)
        return build_balanced_bst(sorted_vals)