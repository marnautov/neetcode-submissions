class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        area = 0

        while left < right:

            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])

            if height[left] <= height[right]:
                area += min(max_left, max_right) - height[left]
                left += 1
            else:
                area += min(max_left, max_right) - height[right]
                right -= 1

        return area

        