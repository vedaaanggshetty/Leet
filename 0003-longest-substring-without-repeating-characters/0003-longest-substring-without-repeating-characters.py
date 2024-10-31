class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index = {}  # Dictionary to store the last index of each character
        max_len = 0
        start = 0  # Start index of the current substring
        
        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                # Move start to the right of the previous index of s[end]
                start = char_index[s[end]] + 1
            # Update the latest index of the character
            char_index[s[end]] = end
            # Calculate the length of the current substring
            max_len = max(max_len, end - start + 1)
        
        return max_len
