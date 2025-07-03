# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def check(node):
            if not node:
                return 0

            left = check(node.left)
            right = check(node.right)

            if left == -1 or right == -1 or abs(right - left ) > 1:
                return -1
            return 1 + max(left, right)
        return check(root) != -1
        
        while que:
            node = que.popleft()
            # Do something with the node...

            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

        return True  # or your actual condition