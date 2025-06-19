# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        que = deque([(root, 1)])
        if not root:
            return 0
        while que:
            node, lvl = que.popleft()
            
            if not node.left and not node.right:
                return lvl
            if node.left : que.append((node.left, lvl + 1))
            if node.right: que.append((node.right, lvl + 1))

            

        return 0

        