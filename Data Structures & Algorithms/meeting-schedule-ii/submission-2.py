"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)

        rooms = 0
        max_rooms = 0
        # stack = []
        heap = []
        heapq.heapify(heap)

        for interval in intervals:

            start = interval.start
            end = interval.end
            
            while heap and heap[0] <= start:
                rooms -= 1
                # stack.pop()
                heapq.heappop(heap)

            rooms += 1
            # stack.append(end)
            heapq.heappush(heap, end)

            max_rooms = max(max_rooms, rooms)

        return max_rooms

            


        