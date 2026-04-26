class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        best_len = 0
        for right, char in enumerate(s):

            if char in seen and seen[char] >= left:
                left = seen[char] + 1

            best_len = max(best_len, right - left + 1)
            
            seen[char] = right

        return best_len
