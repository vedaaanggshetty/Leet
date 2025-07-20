class Solution(object):
    def generateParenthesis(self, n):
        # stack backtracking
        res = []
        stack = []

        def BT(openn, close):
            if openn == close == n:
                res.append("".join(stack))
                return
            
            if openn < n:
                stack.append("(")
                BT(openn+1, close)
                stack.pop()

            if close < openn:
                stack.append(")")
                BT(openn, close + 1)
                stack.pop()

        BT(0,0)
        return res