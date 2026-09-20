class Solution:
    # Time: O(n), Space: O(1)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev1, prev2 = 1, 2

        for _ in range(2, n):
            prev1, prev2 = prev2, prev1 + prev2

        return prev2