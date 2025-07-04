# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        tree = []
        que = deque([root])
        # lvl = 0
        while que:
            n = len(que)
            lvl = []
            for _ in range(n):
                node = que.popleft()
                lvl.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            tree.append(lvl)
        return tree