class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        write = len(nums) - 1

        left, right = 0, len(nums) - 1
        while left <= right:
            square_left = nums[left] ** 2
            square_right = nums[right] ** 2

            if square_right > square_left:
                res[write] = square_right
                right -= 1
            else:
                res[write] = square_left
                left += 1
            write -= 1
            
        return res