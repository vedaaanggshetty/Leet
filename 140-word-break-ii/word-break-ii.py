class Solution(object):
    def wordBreak(self, s, wordDict):
        # using BT recursion 0(2 ^ n * n)
        ss = set(wordDict)
        n = len(s)
        def BT(i):
            if i == n:
                res.append(" ".join(curr))
                return

            for j in range(i, n):
                w = s[i:j+1]
                if w in wordDict:
                    curr.append(w)
                    BT(j+1)
                    curr.pop()

        res = []
        curr = []
        BT(0)
        return res