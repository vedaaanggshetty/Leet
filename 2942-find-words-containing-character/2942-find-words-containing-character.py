class Solution(object):
    def findWordsContaining(self, words, x):
        res = []
        for i,w in enumerate(words):
            if x in w:
                res.append(i)
        return res
        