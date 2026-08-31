class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for act in logs:
            if act == '../':
                if stack:
                    stack.pop()
            elif act != './':
                stack.append(act)

        return len(stack)