class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # nums = [3,1,3,4,2]
        fast, slow = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        finder = nums[0]
        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]

        return finder

