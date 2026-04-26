class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freq = [0] * 26
        for ch in s1:
            freq[ord(ch) - ord('a')] += 1

        left = 0
        missing = len(s1)

        for right in range(0, len(s2)):
            idx = ord(s2[right]) - ord('a')
            if freq[idx] > 0:
                missing -= 1
            freq[idx] -= 1
            if missing == 0:
                return True

            if right - left + 1 == len(s1):
                idx = ord(s2[left]) - ord('a')
                if freq[idx] >= 0:
                    missing += 1

                freq[idx] += 1
                left += 1
        return False



        
        