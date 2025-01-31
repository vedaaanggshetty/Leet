class Solution(object):
    def shuffle(self, nums, n):
        numLen = len(nums)
        # if numLen % 2 != 0:
        #     continue
        j = n
        res=[]
        for i in range(numLen):
            res.append(nums[i])
            res.append(nums[j])
            if(j==numLen-1):
                break
            j=j+1
        return res