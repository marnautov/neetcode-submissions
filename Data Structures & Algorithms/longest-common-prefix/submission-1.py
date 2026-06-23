class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for n in range(len(prefix)):
            for word in strs:
                if not word.startswith(prefix[0:n+1]):
                    return prefix[0:n]
                    
        return prefix
        