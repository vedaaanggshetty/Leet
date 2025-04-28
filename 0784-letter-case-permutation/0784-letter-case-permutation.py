class Solution(object):
    def letterCasePermutation(self, s):
        res = [""]
        for c in s:
            temp  = []
            if c.isalpha():
                for r in res:
                    temp.append(r+c.lower())
                    temp.append(r+c.upper())
            else:
                for r in res:
                    temp.append(r+c)
            res = temp
        return res