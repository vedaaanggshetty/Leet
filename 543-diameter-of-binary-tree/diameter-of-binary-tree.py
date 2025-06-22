# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        # recursive
        self.dia = 0

        def BT(root):
            if not root:
                return False
            
            leftH =  BT(root.left)
            rightH = BT(root.right)

          
            self.dia = max(self.dia, leftH + rightH)
            return 1 + max(leftH, rightH)
        BT(root)
        return self.dia
        