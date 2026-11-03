class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        ir, jr = 0, 0
        i, j = 0, 0

        while ir < len(word1) and jr < len(word2):

            if word1[ir][i] != word2[jr][j]:
                return False

            i += 1
            j += 1

            if i >= len(word1[ir]):
                ir += 1
                i = 0
            
            if j >= len(word2[jr]):
                jr += 1
                j = 0

        return ir == len(word1) and jr == len(word2)




