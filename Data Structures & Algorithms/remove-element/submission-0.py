class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] == val:
                # O(n**2) because of del
                del(nums[idx])
        return len(nums)