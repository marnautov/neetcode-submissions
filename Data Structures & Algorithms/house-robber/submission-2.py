class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0, 0

        for num in nums:
            r1, r2 = r2, max(num + r1, r2)

        return r2