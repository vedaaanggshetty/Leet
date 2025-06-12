class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)+1
        dp = [False] * n
        dp[0] = True
        dicc = set(wordDict)
        for i in range(n):
            for j in range(i):
                if dp[j] and s[j:i] in dicc:
                    dp[i] = True
                    break
        return dp[-1] 