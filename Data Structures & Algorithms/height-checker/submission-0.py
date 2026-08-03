class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        sorted_heights = sorted(heights)

        for idx in range(len(heights)):
            if sorted_heights[idx] != heights[idx]:
                res += 1
        
        return res