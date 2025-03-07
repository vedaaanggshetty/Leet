class Solution(object):
    def removeOuterParentheses(self, s):
        c = 0
        res = ''
        for i in range(len(s)):
            if(s[i] == '('):
                if c > 0:
                    res += s[i]
                c += 1
            else:
                c -= 1
                if c > 0:
                    res += s[i]
        return res