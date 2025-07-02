# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        que = deque([root])
        summ = 0
        while que:
            node = que.popleft()
            if node.left:
                if not node.left.left and not node.left.right:
                    summ += node.left.val
                else:
                    que.append(node.left)
            if node.right:
                que.append(node.right)

        return summ