class Solution(object):
    def reversePrefix(self, word, ch):
        if ch in word:
            # do somethibng
            idx = word.index(ch)
            return ''.join(reversed(word[:idx+1])) + word[idx+1:]
        return word