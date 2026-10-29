class MyHashMap:

    def __init__(self):
        self.size = 1984
        self.map = [[] for _ in range(self.size)]
        
    def _hash(self, key: int) -> int:
        return key % self.size


    def put(self, key: int, value: int) -> None:
        buckets = self.map[self._hash(key)]
        for idx, (k, v) in enumerate(buckets):
            if k == key:
                buckets[idx] = (key, value)
                break
        else:
            buckets.append((key, value))

        
    def get(self, key: int) -> int:
        buckets = self.map[self._hash(key)]
        for k, v in buckets:
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        buckets = self.map[self._hash(key)]
        for idx, (k, v) in enumerate(buckets):
            if k == key:
                del buckets[idx]  


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)