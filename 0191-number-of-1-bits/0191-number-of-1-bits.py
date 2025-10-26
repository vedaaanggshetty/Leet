class Solution(object):
    def hammingWeight(self, n):
        c = 0
        binary = bin(n)[2:]
        c = binary.count('1')
        return c