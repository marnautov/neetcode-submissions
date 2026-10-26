import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Regex solution for variety.
        m = re.search(r"([a-zA-Z]+)\s*$", s)
        return len(m.group(1))