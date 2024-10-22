class Solution(object):
    def maximumOddBinaryNumber(self, s):
        # count = 0
        res = []
        # for i in s:
        #     if i == "1":
        #         count+=1
        #     if count == 1:
        #         res.append(i[-1:])
        #     elif count > 1:
        #         res.append(i[1:-1:])     
        # return res.toString()           

        OneCount = s.count('1')
        if OneCount == 0:
            return s
        
        res =  ['1']*(OneCount - 1) + ['0']*(len(s) - OneCount) + ['1']
           # 1 * (1-1) + 0*3-1 + 1
            # == 001
        return ''.join(res)





        