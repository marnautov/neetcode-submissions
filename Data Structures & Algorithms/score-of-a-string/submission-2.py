class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0

        for idx in range(len(s) - 1):
            res += abs(ord(s[idx + 1]) - ord(s[idx]))

        return res