class Solution(object):
    def romanToInt(self, s):
        dic = {'I' : 1 , 'V' : 5 , 'X' : 10, 'IX' : 9, 'C' : 100, 'L' : 50, 'M' : 1000, 'D' : 500 }
        t = 0
        prev = 0
        for c in reversed(s):
            val = dic[c]

            if val < prev:
                t -= val
            else:
                t += val

            prev = val
        return t                    