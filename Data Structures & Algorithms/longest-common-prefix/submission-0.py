class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for ch in strs[0]:
            prefix += ch
            for word in strs:
                if not word.startswith(prefix):
                    return prefix[:-1]
        return prefix
        