class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0 
        while i < len(s) and j < len(t):
            while j < len(t) and s[i] != t[j]:
                j += 1

            i += 1
            j += 1

        return i == len(s)