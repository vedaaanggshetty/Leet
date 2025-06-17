class Solution(object):
    def isValid(self, s):
        # Stack Approach with 0(1) time lookup

        stack = []
        mapp = { ')' : '(', '}' : '{', ']' : '['}

        for i in s:
            if stack and (i in mapp) and stack[-1] == mapp[i]:
                stack.pop()
            else:
                stack.append(i)
        
        return True if not stack else False