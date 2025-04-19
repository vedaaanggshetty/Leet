class Solution(object):
    def isAnagram(self, s, t):
        # if len(s) != len(t):
        #     return False
        # map = {}
        # for c in s:
        #     if c in map:
        #         map[c] += 1
        #     else:
        #         map[c] = 1
        #     map[c] = map.get(c,0) + 1
        # for c in t:
        #     if c not in map:
        #         return False
        #     map[c] -= 1

        # for c in map.values():
        #     if c != 0:
        #         return False
        # return True
        
        char = [0] * 26
        for c in s:
            char[ord(c) - ord('a')] += 1

        for c in t:
            char[ord(c) - ord('a')] -= 1

        for i in char:
            if i!=0:
                return False
        return True