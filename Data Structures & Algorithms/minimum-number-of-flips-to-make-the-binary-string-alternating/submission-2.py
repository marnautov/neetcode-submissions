class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        doubled = s * 2
        i, j = 0, 0
        min_flips = n

        flips0, flips1 = 0, 0
        while j < len(doubled):
            if doubled[j] != str(j % 2):
                flips0 += 1
            else:
                flips1 += 1

            if j - i + 1 > n:
                if doubled[i] != str(i % 2):
                    flips0 -= 1
                else:
                    flips1 -= 1

                i += 1

            if j - i + 1 == n:
                min_flips = min(min_flips, flips0, flips1)

            j += 1

        return min_flips