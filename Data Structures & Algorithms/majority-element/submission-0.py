class Solution:
    # solution with O(n) time and O(n) space
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        for num, freq in count.items():
            if freq > len(nums) / 2:
                return num