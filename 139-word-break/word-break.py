class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)+1
        dictt = set(wordDict)
        dp = [False]*n
        dp[0] = True
        arr = [0]
        for i in range(n):
            for j in arr:
                if s[j:i] in dictt:
                    dp[i] = True
                    arr.append(i)
                    break
        return dp[-1]