class Solution:
    """
    Simple educational Quick Sort implementation.

    Average time complexity: O(n log n)
    Worst-case time complexity: O(n^2) - only on specifically crafted anti-quicksort inputs

    Average space complexity: O(n) - due to the creation of new lists on each level of the recursion tree
    Worst-case space complexity: O(n^2) - if the recursion tree degenerates into a linear chain of O(n) depth
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        pivot = nums[len(nums) // 2]

        less = []
        greater = []
        equal = []

        for num in nums:
            if num > pivot:
                greater.append(num)
            elif num < pivot:
                less.append(num)
            else:
                equal.append(num)
        
        return self.sortArray(less) + equal + self.sortArray(greater)