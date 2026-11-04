class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack and ch.swapcase() == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)

