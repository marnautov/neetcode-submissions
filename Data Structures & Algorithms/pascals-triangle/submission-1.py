class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(1, numRows):
            res.append([1])

            for j in range(1, i):
                prev = res[i - 1]

                left = prev[j - 1]
                right = prev[j]

                res[i].append(left + right)
            res[i].append(1)

        return res





        