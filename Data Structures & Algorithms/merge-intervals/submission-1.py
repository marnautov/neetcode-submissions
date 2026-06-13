class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x:x[0])
        new_start, new_end = intervals[0]
        
        for i, (start, end) in enumerate(intervals):
            if start <= new_end:
                new_start = min(new_start, start)
                new_end = max(new_end, end)
            else:
               res.append([new_start, new_end])
               new_start, new_end = start, end 
        res.append([new_start, new_end])
        return res


        