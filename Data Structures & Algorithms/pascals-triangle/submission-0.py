class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for numRow in range(1, numRows):
            res.append([])

            for num in range(numRow + 1):
                prev_left = res[numRow - 1][num - 1] if num > 0 else 0
                prev_right = res[numRow - 1][num] if num < numRow else 0

                res[numRow].append(prev_left + prev_right)

        return res