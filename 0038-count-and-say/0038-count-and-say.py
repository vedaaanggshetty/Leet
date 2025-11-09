class Solution(object):
    def countAndSay(self, n):
        mapp = {}
        s = "1"
        for _ in range(n-1):
            new = ""
            count = 1
            for j in range(1, len(s) + 1):
                if j < len(s) and s[j] == s[j-1]:
                    count += 1
                else:
                    mapp[s[j-1]] = count
                    new += str(count) + s[j-1]
                    count = 1
            s = new
        return s