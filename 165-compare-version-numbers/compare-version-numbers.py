class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = (version1.split('.'))
        v2 = (version2.split('.'))
        
        n = max(len(v1), len(v2))
        for i in range(n):
            s1 = int(v1[i]) if i < len(v1) else 0
            s2 = int(v2[i]) if i < len(v2) else 0

            if s1 < s2: return -1
            elif s1 > s2: return 1
        return 0