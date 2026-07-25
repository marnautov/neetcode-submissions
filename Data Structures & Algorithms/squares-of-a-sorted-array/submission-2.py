class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []

        right = 0
        while right < len(nums) and nums[right] < 0:
            right += 1

        left = right - 1
        while left >= 0 or right < len(nums):

            if right >= len(nums):
                result.append(nums[left] ** 2)
                left -= 1
                continue

            if left < 0:
                result.append(nums[right] ** 2)
                right += 1
                continue

            power_left = nums[left] ** 2
            power_right = nums[right] ** 2
            if power_left <= power_right:
                result.append(power_left)
                left -= 1
            else:
                result.append(power_right)
                right += 1

        return result

            

