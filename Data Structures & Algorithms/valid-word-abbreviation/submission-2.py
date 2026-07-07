class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit() and abbr[j] != "0":

                start = j
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                l = int(abbr[start:j])

                i += l

            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        
        return True if i == len(word) and j == len(abbr) else False

