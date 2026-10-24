class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Time: O(n + m), Space: O(n + m)
        def process(string: str) -> list[str]:
            stack = []

            for ch in string:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
        
            return stack

        return process(s) == process(t)