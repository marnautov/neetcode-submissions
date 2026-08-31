class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0

        for act in logs:
            if act == '../':
                if depth > 0:
                    depth -= 1
            elif act != './':
                depth += 1

        return depth