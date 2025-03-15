class Solution(object):
    def minimumAbsDifference(self, arr):
        # ill sort it first
        arr.sort()

        # find min
        res = [] 
        n = len(arr)
        minD = float('inf')
        for i in range(1,n):
            minD = min(minD, arr[i]-arr[i-1])

        # append
        for i in range(1, n):
            if (arr[i] - arr[i-1]) == minD:
                res.append([arr[i-1], arr[i]])
        return res