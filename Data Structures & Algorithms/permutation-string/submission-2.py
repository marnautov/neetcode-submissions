class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0] * 26

        for ch in s1:
            freq[ord(ch) - ord('a')] += 1

        left = 0
        for right, ch in enumerate(s2):
            idx = ord(ch) - ord('a')
            freq[idx] -= 1

            while freq[idx] < 0:
                freq[ord(s2[left]) - ord('a')] += 1
                left += 1

            if right - left + 1 == len(s1):
                return True

        return False
        