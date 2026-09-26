class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def max_rob(houses: List[int]):
            if len(houses) == 1:
                return houses[0]

            dp = [houses[0], max(houses[0], houses[1])]

            for i in range(2, len(houses)):
                dp.append(max(dp[i - 2] + houses[i], dp[i - 1]))

            return dp[-1]

        return max(
            max_rob(nums[1:]),
            max_rob(nums[:-1])
        )
