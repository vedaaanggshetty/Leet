class Solution(object):
    def sortEvenOdd(self, nums):
        even = [nums[i] for i in range(len(nums)) if i % 2 == 0]
        odd = [nums[i] for i in range(len(nums)) if i % 2 ==1]

        even.sort()
        odd.sort(reverse = True)
        neww = []
        eve = 0
        od = 0
        #  nums = [4,1,2,3]
         # eve = [2,4]
        #  odd = [3,1]
    # new = []
        for i in range(len(nums)):
            if(i % 2 == 0):
                    neww.append(even[eve])
                    eve +=1
            else:
                    neww.append(odd[od])
                    od +=1
        return neww