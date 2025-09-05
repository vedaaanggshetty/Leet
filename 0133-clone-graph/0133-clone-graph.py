"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):

        if not node:
            return None

        que = collections.deque([node])
        mapp = {node : Node(node.val)}

        while que:
            curr = que.popleft()
            for n in curr.neighbors:
                if n not in mapp:
                    mapp[n] = Node(n.val)
                    que.append(n)
                
                mapp[curr].neighbors.append(mapp[n])
        return mapp[node]
