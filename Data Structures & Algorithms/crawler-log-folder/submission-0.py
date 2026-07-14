class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0

        for cmd in logs:
            if cmd == '../':
                if level > 0:
                    level -= 1
            elif cmd == './':
                pass
            else:
                level += 1

        return level

        