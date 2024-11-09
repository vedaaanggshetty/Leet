class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2

        # Initialize the base cases for n = 1 and n = 2
        first = 1
        second = 2
        
        # Iterate from 3 to n, updating the number of ways dynamically
        for i in range(3, n + 1):
            current = first + second
            first = second
            second = current
        
        return second
