class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        q = deque()

        for right in arr:
            diff = abs(right - x)
            q.append((diff, right))
            
            if len(q) > k:
                if q[-1][0] < q[0][0]:
                    q.popleft()
                else:
                    q.pop()
                    # break

        return [value for _, value in q]