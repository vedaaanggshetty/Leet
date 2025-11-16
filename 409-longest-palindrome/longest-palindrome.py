class Solution(object):
    def longestPalindrome(self, s):
        mapp = {}
        for c in s:
            mapp[c] = mapp.get(c,0) + 1

        res = 0
        odd = False

        for count in mapp.values():
            res += (count // 2) * 2

            if count % 2 == 1: odd = True

        if odd: res += 1
        return res