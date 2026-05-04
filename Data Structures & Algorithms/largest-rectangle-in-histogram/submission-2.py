class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0

        for i, h in enumerate(heights):
            start = i
            # use >= to collapse duplicate heights and keep the earliest start index.
            # using > also works, but keeps duplicates in the stack.
            while stack and stack[-1][1] >= h:
                old_i, old_h = stack.pop()
                area = (i - old_i) * old_h
                largest = max(largest, area)
                start = old_i
            stack.append((start, h))
        
        while stack:
            old_i, old_h = stack.pop()
            area = (len(heights) - old_i) * old_h
            largest = max(largest, area)
        
        return largest