class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        for i, word in enumerate(words):
            for j, other in enumerate(words):
                if i != j and word in other:
                    res.append(word)
                    break

        return res