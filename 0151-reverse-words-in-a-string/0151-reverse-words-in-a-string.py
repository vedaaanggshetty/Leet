class Solution(object):
    def reverseWords(self, s):
     # Remove leading/trailing spaces
        s = s.strip()
        # Split the string into words
        words = s.split()
        # Reverse the list of words
        reversed_words = words[::-1]
        # Join the reversed words into a single string
        result = " ".join(reversed_words)
        return result