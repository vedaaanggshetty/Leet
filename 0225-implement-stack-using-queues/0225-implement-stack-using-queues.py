
class MyStack(object):

    def __init__(self):
        self.que = deque()

    def push(self, x):
        self.que.append(x)
        

    def pop(self):
        for i in range(len(self.que)-1):
            self.push(self.que.popleft())
        return self.que.popleft()

    def top(self):
        return self.que[-1]
        
    def empty(self):
        return len(self.que) == 0
que = MyStack()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()