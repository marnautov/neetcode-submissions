class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_left = 0
        best_right = 0

        def expand(left: int, right: int) -> None:
            nonlocal best_left, best_right

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left > best_right - best_left:
                    best_left = left
                    best_right = right

                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return s[best_left:best_right + 1]