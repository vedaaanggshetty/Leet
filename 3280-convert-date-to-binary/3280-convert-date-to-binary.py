class Solution(object):
        def convertDateToBinary(self, date):
            lst = date.split("-")
            res = []
            for n in lst:
                res.append(bin(int(n))[2:])
            return "-".join(res)
