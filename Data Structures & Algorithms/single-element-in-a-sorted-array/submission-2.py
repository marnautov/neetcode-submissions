class Solution:
    # Bitwise XOR solution - O(n)
    def singleNonDuplicate(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result