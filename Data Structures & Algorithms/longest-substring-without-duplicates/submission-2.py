class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = {}
        left = 0

        for right, ch in enumerate(s):
            last_seen = seen.get(ch, -1)

            if last_seen >= left:
                left = last_seen + 1
            
            seen[ch] = right
            longest = max(longest, right - left + 1)
        
        return longest
        