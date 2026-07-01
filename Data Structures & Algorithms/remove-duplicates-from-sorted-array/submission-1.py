class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0

        for num in nums:
            if num != nums[write]:
                write += 1
                
            nums[write] = num
        
        return write + 1
        