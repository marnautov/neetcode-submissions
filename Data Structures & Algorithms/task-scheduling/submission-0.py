class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        heap = []
        for task, count in freq.items():
            heapq.heappush(heap, (-count, task))

        cooldown = deque()
        time = 0

        while heap or cooldown:
            time += 1
            if heap:
                count, task = heapq.heappop(heap)
                count += 1

                if count < 0:
                    cooldown.append((time + n, count, task))

            if cooldown and cooldown[0][0] == time:
                _, count, task = cooldown.popleft()
                heapq.heappush(heap, (count, task))

        return time