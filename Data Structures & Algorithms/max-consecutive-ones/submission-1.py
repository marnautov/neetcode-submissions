class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        
        current_len = 0
        for num in nums:
            if num == 1:
                current_len += 1
                if current_len > max_len:
                    max_len = current_len
            else:
                current_len = 0
        
        return max_len