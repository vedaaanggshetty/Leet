# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        # same as the levels of BT but instead you add more tuples
        que = deque([root])
        res = []
        if not root:
            return []
        while que:
            lvl = []
            for i in range(len(que)):
                node = que.popleft()
                lvl.append(node.val)

                if node.left : que.append(node.left)
                if node.right : que.append(node.right)

            res.append(lvl)
        return res