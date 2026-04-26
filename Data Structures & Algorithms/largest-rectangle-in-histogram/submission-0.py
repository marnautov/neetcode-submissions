class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        left = [-1] * n
        right = [n] * n

        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                right[stack[-1]] = i
                stack.pop()
            stack.append(i)

        area_max = 0
        for i in range(n):
            area = heights[i] * (right[i] - left[i] - 1)
            area_max = max(area_max, area)
        
        return area_max
        