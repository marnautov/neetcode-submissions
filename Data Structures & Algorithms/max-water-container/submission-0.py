class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        left, right = 0, len(heights) - 1
        while left < right:
            maximum = max(maximum, (right - left) * min(heights[right], heights[left]))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maximum 