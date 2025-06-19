# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        que = deque([root])
  #     print(que)
        res = []     

        while que:
            lvl = []
            for i in range(len(que)):
                node = que.popleft()
                lvl.append(node.val)
                if node.left : que.append(node.left)
                if node.right : que.append(node.right)
            res.append(float(sum(lvl))/len(lvl))        
        return res