class Solution(object):
    def combine(self, n, k):
        def BT(s,p):
            if k == len(p):
                res.append(p[:])
                return
            for i in range(s,n+1):
                p.append(i)
                BT(i+1, p)
                p.pop()
        res = []
        BT(1, [])
        return res    