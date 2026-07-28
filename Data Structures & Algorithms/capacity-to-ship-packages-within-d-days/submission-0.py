class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2

            days_needed = 1
            total = 0
            for weight in weights:
                total += weight
                if total > mid:
                    days_needed += 1
                    total = weight

            if days_needed <= days:
                right = mid
            else:
                left = mid + 1

        return right
        