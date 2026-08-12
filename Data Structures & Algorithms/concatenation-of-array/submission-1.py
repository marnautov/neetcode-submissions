class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * (n * 2)

        for idx, num in enumerate(nums):
            res[idx] = num
            res[idx + n] = num

        return res
        