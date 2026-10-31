class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def next_char(items: list[str]) -> Generator:
            for item in items:
                for ch in item:
                    yield ch

        gen1 = next_char(word1)
        gen2 = next_char(word2)

        while True:
            ch1 = next(gen1, None)
            ch2 = next(gen2, None)
            if ch1 != ch2:
                return False

            if ch1 is None:
                return True


