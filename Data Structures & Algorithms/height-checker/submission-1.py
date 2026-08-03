class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0

        for expected, actual in zip(sorted(heights), heights):
            if expected != actual:
                count += 1

        return count
        