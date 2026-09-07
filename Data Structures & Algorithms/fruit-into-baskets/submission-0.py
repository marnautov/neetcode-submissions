class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        types = defaultdict(int)
        max_len = 0

        for right in range(len(fruits)):
            types[fruits[right]] += 1

            while len(types) > 2:
                types[fruits[left]] -= 1

                if types[fruits[left]] <= 0:
                    del types[fruits[left]]

                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

        