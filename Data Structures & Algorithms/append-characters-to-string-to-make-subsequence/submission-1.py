class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        res = 0
        while j < len(t):
            if i >= len(s):
                res = len(t) - j
                return res
            if s[i] == t[j]:
                j += 1
            i += 1
        return res
        