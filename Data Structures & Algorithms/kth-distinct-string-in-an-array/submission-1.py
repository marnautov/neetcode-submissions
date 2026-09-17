from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)

        for item, freq in count.items():
            if freq == 1:
                k -= 1
                if k == 0:
                    return item

        return ""
        