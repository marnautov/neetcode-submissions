class Solution:
    def decodeString(self, s: str) -> str:
        # Regex solution for a change
        while '[' in s:
            s = re.sub(
                r'(\d+)\[([a-z]+)\]', 
                lambda x: x.group(2) * int(x.group(1)), 
                s
            )
        return s
        