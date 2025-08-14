from collections import Counter
class Solution(object):
    def canArrange(self, arr, k):
        # que = deque([arr])
        # res = []
        
        # def BT(pair, tar):
        #     node = que.popleft()
        #     if node == tar:
        #         return True
            
        #     else:
        #         res.append(node)
        #         tar += node.val
        
        r = Counter([n % k for n in arr])

        if r[0] % 2 != 0:
            return False

        
        for i in range(1, k):
            if i == k - i:
                if r[i] % 2 != 0:
                    return False

            else:
                if r[i] != r[k-i]:
                    return False
        return True


