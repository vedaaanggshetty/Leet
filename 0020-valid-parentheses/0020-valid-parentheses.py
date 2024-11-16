class Solution(object):
    def isValid(self, s):
         stack = []
         open = { ")" : "(" , "]" : "[" , "}" : "{" }

         for c in s:
            if c in open:
                if stack and stack[-1] == open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
         
         return True if not stack else False