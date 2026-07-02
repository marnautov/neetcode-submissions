class Solution:
    """
    Bubble sort implementation 

    Time complexity: O(n²)
    Space complexity: O(1)
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        swapped = True

        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True
                    
        return nums