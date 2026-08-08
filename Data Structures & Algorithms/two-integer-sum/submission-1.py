class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for idx, num in enumerate(nums):
            if num in seen:
                return [seen[num], idx]
            seen[target - num] = idx

