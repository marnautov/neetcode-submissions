class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # left range
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if left >= len(nums) or nums[left] != target:
            return [-1, -1]

        range_left = left

        # right range        
        left, right = range_left, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        range_right = right

        return [range_left, range_right]
