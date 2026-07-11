class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, (n // 2) + 1

        while left <= right:
            mid = (left + right) // 2
            result = mid * (mid + 1) // 2

            if result > n:
                right = mid - 1
            else:
                left = mid + 1
        
        return right


        