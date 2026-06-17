class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            speed = (left + right) // 2
            hours = sum( (bananas + speed - 1) // speed for bananas in piles)
            if hours <= h:
                right = speed
            else:
                left = speed + 1
        return right


        