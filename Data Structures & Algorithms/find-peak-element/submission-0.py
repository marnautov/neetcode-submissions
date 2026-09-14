class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            left_mid = nums[mid - 1] if mid else float('-inf')
            right_mid = nums[mid + 1] if mid < len(nums) - 1 else float('-inf')

            if left_mid < nums[mid] > right_mid:
                return mid

            if right_mid > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1
        