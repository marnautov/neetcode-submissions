class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 0
        max_pal = ''

        dp = [[False] * n for _ in range(n)]
        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                
                if length == 1:
                    dp[left][right] = True
                elif length == 2:
                    dp[left][right] = s[left] == s[right]
                else:
                    dp[left][right] = s[left] == s[right] and dp[left + 1][right -1]

                if dp[left][right] and length > max_len:
                    max_len = length
                    max_pal = s[left:right+1]

        return max_pal