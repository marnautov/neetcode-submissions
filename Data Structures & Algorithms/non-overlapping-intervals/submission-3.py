class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        count = 0
        prev_start, prev_end = intervals[0]

        for start, end in intervals[1:]:
            if start < prev_end:
                count += 1
                prev_end = min (prev_end, end)
            else:
                prev_end = end
                
        return count
        