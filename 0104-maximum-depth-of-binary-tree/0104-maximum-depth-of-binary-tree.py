# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
       #since the root node is marked 1
        que = deque([(root,1)])
        if not root:
            return 0
        while que:
            node, lev = que.popleft()    
            if node.left : que.append((node.left, lev+1))
            if node.right : que.append((node.right, lev+1))

        return lev

       
        