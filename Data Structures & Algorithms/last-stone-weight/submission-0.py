class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            s1 = abs(heapq.heappop(heap))
            s2 = abs(heapq.heappop(heap))
            if s1 > s2:
                heapq.heappush(heap, -(s1 - s2))
            
        return abs(heap[0]) if heap else 0
