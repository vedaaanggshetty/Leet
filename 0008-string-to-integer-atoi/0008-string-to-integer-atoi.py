class Solution(object):
    def myAtoi(self, s):
        if not s:  # Edge case: Empty string
            return 0

        # Step 1: Trim leading whitespaces
        s = s.lstrip()

        if not s:  # If string is empty after stripping
            return 0

        # Step 2: Handle sign
        sign = 1
        if s[0] in ('-', '+'):
            if s[0] == '-':
                sign = -1
            s = s[1:]

        # Step 3: Convert digits into number
        res = 0
        for char in s:
            if char.isdigit():
                res = res * 10 + int(char)  # Correct formula
            else:
                break

        # Step 4: Apply sign
        res *= sign

        # Step 5: Handle integer overflow
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX

        return res
