class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left, right = 0, 0
        n = len(nums)
        need = sum(nums) - x

        if need < 0:
            return -1

        total = 0
        min_steps = float('inf')

        while left <= right:
            if total == need:
                min_steps = min(min_steps, n - (right - left))

            if total < need and right < n:
                total += nums[right]
                right += 1
            elif left < right:
                total -= nums[left]
                left += 1
            else:
                break

            
        return min_steps if min_steps != float('inf') else -1




