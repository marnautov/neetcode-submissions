class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x = abs(nums[i])
            idx = x - 1
            if nums[idx] < 0:
                return x
            nums[idx] *= -1
        