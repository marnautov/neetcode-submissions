class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        count = sum(ch in vowels for ch in s[:k])
        best = count

        for i in range(k, len(s)):
            count += (s[i] in vowels) - (s[i - k] in vowels)
            best = max(best, count)

        return best