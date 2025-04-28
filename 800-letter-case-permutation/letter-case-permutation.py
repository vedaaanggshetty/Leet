class Solution(object):
    def letterCasePermutation(self, s):
        res = [""]
        for c in s:
            temp = []
            for r in res:
                if c.isalpha():
                    temp.append(r + c.lower())
                    temp.append(r + c.upper())
                else:
                    temp.append(r + c)
            res = temp
        return res