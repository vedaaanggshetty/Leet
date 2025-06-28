class Solution(object):
    def reverse(self, x):
        maxx = 2 ** 31 - 1
        minn = -2 ** 31 
        rev = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x!=0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x //10

        rev *= sign
        if rev > maxx or rev < minn:
            return 0
        return rev