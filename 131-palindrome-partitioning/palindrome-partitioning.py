class Solution(object):
    def partition(self, s):
        res = []
        # curr = []
        def isPal(sub):
            return sub == sub[::-1]
        def BT(start, curr):
            if start == len(s):
                res.append(list(curr))
                return            

            for i in range(start + 1, len(s) + 1):
                subS = s[start:i]
                if isPal(subS):
                    curr.append(subS)
                    BT(i, curr)
                    curr.pop()

            
        BT(0, [])
        return res