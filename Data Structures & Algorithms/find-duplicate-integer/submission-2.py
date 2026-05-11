class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        fast, slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        finder = 0
        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]
            
        return finder