class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        import math
        maxxArea = 0
        maxxSqr = 0
        for l, b in dimensions:
            diag = ( l ** 2 ) + ( b ** 2)
            area = l * b

            if diag > maxxSqr:
                maxxSqr = diag
                maxxArea = area
            elif diag == maxxSqr:
                maxxArea = max(maxxArea, area)
        return maxxArea