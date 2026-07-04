import random

class Solution:

    def partition(self, nums: List[int], left: int, right: int) -> int:

        random_idx = random.randint(left, right)
        nums[random_idx], nums[right] = nums[right], nums[random_idx]

        pivot = nums[right]

        i = left
        for j in range(left, right):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        
        nums[i], nums[right] = nums[right], nums[i]

        return i


    def quickSort(self, nums: List[int], left: int, right: int) -> None:
        if left >= right:
            return

        pivot_index = self.partition(nums, left, right)
        self.quickSort(nums, left, pivot_index - 1)
        self.quickSort(nums, pivot_index + 1, right)


    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums