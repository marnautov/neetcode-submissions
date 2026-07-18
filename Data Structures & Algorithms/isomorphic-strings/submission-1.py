class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = dict()
        used = set()
        
        for i in range(0, len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                if t[i] in used:
                    return False
                
                mapping[s[i]] = t[i]
                used.add(t[i])
        
        return True
        