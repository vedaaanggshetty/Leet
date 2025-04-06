class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        mapST = {}
        mapTS = {}
        for i,j in zip(s,t):
            if i in mapST:
                if mapST[i] != j:
                    return False
            else:
                mapST[i] = j
            if j in mapTS:
                if mapTS[j] != i:
                    return False
            else:
                mapTS[j] = i
        return True
        