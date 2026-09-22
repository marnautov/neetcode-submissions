class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        two_prev = nums[0]
        one_prev = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            two_prev, one_prev = one_prev, max(one_prev, two_prev + nums[i])

        return one_prev