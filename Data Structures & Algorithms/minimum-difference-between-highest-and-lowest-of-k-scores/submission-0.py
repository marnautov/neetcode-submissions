class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_diff = float('inf')

        i, j = 0, k - 1
        while j < len(nums):
            min_diff = min(min_diff, nums[j] - nums[i])
            i += 1
            j += 1

        return min_diff