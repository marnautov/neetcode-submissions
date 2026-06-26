class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(left: int, right: int):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                if isValid(left + 1, right) or isValid(left, right - 1):
                    return True
                return False
            
            left += 1
            right -= 1

        return True
        