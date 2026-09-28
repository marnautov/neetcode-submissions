class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        
        def expand(left: int, right: int) -> None:
            nonlocal result

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(result):
                    result = s[left:right + 1]

                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return result