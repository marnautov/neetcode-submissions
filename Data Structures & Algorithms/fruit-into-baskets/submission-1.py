class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        types = defaultdict(int)
        max_len = 0

        for r in range(len(fruits)):
            types[fruits[r]] += 1

            while len(types) > 2:

                if types[fruits[l]] == 1:
                    del types[fruits[l]]
                else:
                    types[fruits[l]] -= 1

                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len

        