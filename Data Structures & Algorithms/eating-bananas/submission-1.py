class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            total = sum((i + mid - 1) // mid for i in piles)
            if total <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left