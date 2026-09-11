class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:    
        res = sorted(arr, key = lambda v: (abs(x - v), v))
        return sorted(res[0:k])