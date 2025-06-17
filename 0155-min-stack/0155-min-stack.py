class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        if not self.stack:
            currMin = val
        else:
            currMin = min(val, self.stack[-1][-1])    
        self.stack.append((val,currMin))

    def pop(self):
        self.stack.pop()
        
    def top(self):
        return self.stack[-1][0]
    
    def getMin(self):
        return self.stack[-1][-1]

#minStack = MinStack()
#inStack.push(-2)
#minStack.pop()    


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()