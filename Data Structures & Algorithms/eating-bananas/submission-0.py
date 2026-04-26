class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)
        best = right

        while left <= right:

            guess_speed = (left + right) // 2
            hours = sum((x + guess_speed - 1) // guess_speed for x in piles)

            if hours <= h:
                best = guess_speed
                right = guess_speed - 1
            else:
                left = guess_speed + 1

        return best