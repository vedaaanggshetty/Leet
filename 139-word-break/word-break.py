class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)+1
        # dictt = set(wordDict)
        dp = [False]*n
        dp[0] = True
        # arr = [0]
        for i in range(n):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    # arr.append(i)
                    break
        return dp[-1]