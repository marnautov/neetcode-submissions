class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] % 2 == 0:
                left += 1
                continue
            if nums[right] % 2 != 0:
                right -= 1
                continue
            nums[left], nums[right] = nums[right], nums[left]

        return nums
            
        