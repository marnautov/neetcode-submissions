class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0

        for idx in range(len(s) - 1, -1, -1):
            char = s[idx]
            if char.isspace():
                if length > 0:
                    return length
            else:
                length += 1
        
        return length

        