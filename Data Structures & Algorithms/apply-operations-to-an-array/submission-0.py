class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        i = 0
        j = 0

        while i < len(nums):
            if i == len(nums) - 1:
                res[j] = nums[i]
                break

            if nums[i] == 0:
                i += 1
                continue

            if nums[i] == nums[i + 1]:
                res[j] = nums[i] * 2
                i += 1
            else:
                res[j] = nums[i]

            i += 1
            j += 1

        return res

        
            
