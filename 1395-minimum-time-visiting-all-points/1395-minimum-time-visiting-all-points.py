class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        x1, y1 = points.pop()
        second = 0
        while points:
            x2, y2 = points.pop()
            second += max(abs(y2-y1), abs(x2-x1))
            x1, y1 = x2 ,y2
        return second