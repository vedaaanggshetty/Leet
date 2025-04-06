class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        double = s + s
        return goal in double