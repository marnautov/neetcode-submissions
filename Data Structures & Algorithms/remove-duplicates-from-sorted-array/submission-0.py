class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        for i, ch in enumerate(nums):
            if ch != nums[write]:
                write += 1
            nums[write] = ch
        return write + 1