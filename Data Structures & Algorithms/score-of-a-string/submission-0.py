class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for idx in range(0, len(s) - 1):
            total += abs(ord(s[idx + 1]) - ord(s[idx]))
        return total