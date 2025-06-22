# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        # recursive
        # self.dia = 0

        # def BT(root):
        #     if not root:
        #         return False
            
        #     leftH =  BT(root.left)
        #     rightH = BT(root.right)

          
        #     self.dia = max(self.dia, leftH + rightH)
        #     return 1 + max(leftH, rightH)
        # BT(root)
        # return self.dia
        
        # Iterative
        s = [(root, False)]
        dia = 0
        maxx = {}
        while s:
            n,v = s.pop()

            if not v:
                s.append((n, True))
                if n.left:
                    s.append((n.left, False))
                if n.right:
                    s.append((n.right, False))
            
            else:
                if not n.left:
                    leftH = 0
                else:
                    leftH = maxx.pop(n.left)
                
                if not n.right:
                    rightH = 0
                else:
                    rightH = maxx.pop(n.right)

                dia = max(dia, leftH + rightH)
                maxx[n] = max(leftH, rightH) + 1
        return dia
                