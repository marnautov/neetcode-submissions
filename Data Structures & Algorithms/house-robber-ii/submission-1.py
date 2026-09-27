class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def max_rob(start, stop):
            one_prev = 0
            two_prev = 0
            
            for i in range(start,stop):
                one_prev, two_prev = max(two_prev + nums[i], one_prev), one_prev 

            return one_prev

        return max(
            max_rob(1, len(nums)), 
            max_rob(0, len(nums) - 1)
            )