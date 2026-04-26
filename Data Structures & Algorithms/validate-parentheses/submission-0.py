class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {'(':')', '[':']', '{':'}'}
        stack = []
        for char in s:
            
            if char in char_map:
                stack.append(char_map[char])
                continue
            
            if not stack or char != stack.pop():
                return False
            
        return True if not stack else False

        