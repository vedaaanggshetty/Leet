class Solution(object):
    def hammingWeight(self, n):
        c = 0
        binary = bin(n)[2:]
        for i in list(binary):
            if i == '1':
                c += 1
        return c