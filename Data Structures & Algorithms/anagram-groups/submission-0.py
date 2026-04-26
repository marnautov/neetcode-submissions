from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        items = defaultdict(list)
        for string in strs:
            key = ''.join(sorted(string))
            items[key].append(string)
        return list(items.values())
            