class Solution(object):
    def maxDepth(self, s):
        # Initialize variables for current depth and max depth
        current_depth = 0
        max_depth = 0
        
        # Iterate through the string
        for char in s:
            if char == '(':
                # Increase current depth
                current_depth += 1
                # Update max depth if needed
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                # Decrease current depth
                current_depth -= 1

        return max_depth
