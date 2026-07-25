class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []

        right = 0
        while right < len(nums) and nums[right] < 0:
            right += 1

        left = right - 1
        while left >= 0 or right < len(nums):

            square_left = nums[left] ** 2 if left >= 0 else float('inf')
            square_right = nums[right] ** 2 if right < len(nums) else float('inf')

            if square_left <= square_right:
                result.append(square_left)
                left -= 1
            else:
                result.append(square_right)
                right += 1

        return result

            

