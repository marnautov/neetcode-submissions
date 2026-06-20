class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ''

        count: dict[str, int] = dict()
        for ch in t:
            count[ch] = count.get(ch, 0) + 1

        need = len(count)
        have = 0

        left = 0
        for right, char in enumerate(s):

            if char in count:
                count[char] -= 1
                if count[char] == 0:
                    have += 1

                while have == need:

                    if not res or right - left + 1 < len(res):
                        res = s[left:right + 1]

                    left_char = s[left]

                    if left_char in count:
                        count[left_char] += 1
                        if count[left_char] > 0:
                            have -= 1
                    
                    left += 1

        return res



        