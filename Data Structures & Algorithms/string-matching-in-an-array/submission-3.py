class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()

        for i, word in enumerate(words):
            for other in words[i + 1:]:
                if word in other:
                    res.add(word)
                if other in word:
                    res.add(other)

        return list(res)