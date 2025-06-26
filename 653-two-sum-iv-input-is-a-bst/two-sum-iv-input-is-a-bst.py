# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        # BFS
        que = deque([root])
        numS = set()
        while que:
            node = que.popleft()
            if (k-node.val) in numS:
                return True
            else:
                numS.add(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)        
        return False
