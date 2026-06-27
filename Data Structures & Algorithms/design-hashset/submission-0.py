class MyHashSet:

    def __init__(self):
        self.size = 6767
        self.buckets = [[] for _ in range(self.size)]
        
    def add(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, item in enumerate(bucket):
            if item == key:
                del bucket[i]
                return

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for item in bucket:
            if item == key:
                return True
        return False

    def _hash(self, key: int) -> int:
        return key % self.size

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)