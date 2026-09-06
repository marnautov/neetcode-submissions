class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        total = 0
        min_freq = float('inf')

        while j < len(nums):
            total += nums[j]
            j += 1

            while total >= target:
                min_freq = min(min_freq, j - i)
                total -= nums[i]
                i += 1

        return min_freq if min_freq != float('inf') else 0
