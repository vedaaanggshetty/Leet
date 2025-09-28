class Solution(object):
    def largestTriangleArea(self, points):
        def area(p1,p2,p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3

            return 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

        maxx = 0
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    maxx = max(maxx , area(points[i], points[j], points[k]))

        return maxx