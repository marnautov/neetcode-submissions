class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        count = sum(s[x] in vowels for x in range(k))
        best = count

        for n in range(len(s) - k):
            if s[n] in vowels:
                count -= 1
            if s[n + k] in vowels:
                count += 1
            best = max(best, count)

        return best



