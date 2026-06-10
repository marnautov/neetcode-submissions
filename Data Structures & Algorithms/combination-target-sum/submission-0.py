class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(idx: int, current_sum: int) -> None:

            if idx >= len(nums):
                return

            if current_sum > target:
                return

            if current_sum == target:
                res.append(path.copy())
                return


            path.append(nums[idx])
            dfs(idx, current_sum + nums[idx])

            path.pop()
            dfs(idx + 1, current_sum)
            
            
        dfs(0, 0)

        return res
        