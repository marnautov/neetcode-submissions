class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        max_freq = 1
        left = 0
        for right in range(1, len(nums)):
            diff = nums[right] - nums[right - 1]

            k -= diff * (right - left)

            while k < 0:
                k += nums[right] - nums[left]
                left += 1
            
            max_freq = max(max_freq, right - left + 1)

        return max_freq