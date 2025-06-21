# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        s = [(p,q)]
        while s:
            n1,n2 = s.pop()
            if not n1 and not n2:
                continue
            if None in [n1,n2] or n1.val != n2.val:
                return False
            s.append((n1.left, n2.left))
            s.append((n1.right, n2.right))

        return True