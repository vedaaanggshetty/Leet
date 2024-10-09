class Solution(object):
    def isAcronym(self, words, s):
        acr = []
        for word in words:
            acr.append(word[0])  # abc
        acronym = ''.join(acr)  # becomes "abc"
        if acronym == s:
            return True
        return False
    #   return acronym == s