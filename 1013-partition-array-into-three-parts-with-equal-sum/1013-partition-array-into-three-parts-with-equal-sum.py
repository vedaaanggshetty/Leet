class Solution(object):
    def canThreePartsEqualSum(self, arr):
        total = sum(arr)
        curr = 0
        count = 0
        if(total % 3 != 0):
            return False
        actual = total//3
        for i in range(len(arr)):
            curr += arr[i]
            if(curr == actual):
                curr = 0
                count+=1    
            if count == 2 and i <  len(arr) - 1:
                return True
        return False     



