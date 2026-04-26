class Solution:
    def trap(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0
        while left < right:

            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)

            if left_max < right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1
        return water



        