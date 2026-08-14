class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count = Counter(t)

        for char in s:
            if char not in count or count[char] <= 0:
                return False

            count[char] -= 1

        return True