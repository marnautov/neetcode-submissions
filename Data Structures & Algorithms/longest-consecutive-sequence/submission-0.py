class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        for n in nums:
            if n - 1 not in nums:
                current = n
                while current + 1 in nums:
                    current += 1
                max_len = max(max_len, current - n + 1)
        return max_len
        