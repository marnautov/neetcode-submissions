class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map.setdefault(key, []).append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        buckets = self.map[key]
        left, right = 0, len(buckets) - 1
        while left <= right:
            mid = (left + right) // 2
            if buckets[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return buckets[right][1] if right >= 0 else ""
        
