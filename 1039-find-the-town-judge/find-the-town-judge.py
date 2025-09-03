class Solution(object):
    def findJudge(self, n, trust):
        # so no cycle? in a DAG?
        count = [0] * (n+1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1 

        for i in range(1, n+1):
            if count[i] == n - 1:
                return i
        return -1