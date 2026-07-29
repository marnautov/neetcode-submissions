class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i, j = 0, 0
        op = 0

        while j < k:
            op += 1 if blocks[j] == 'W' else 0
            j += 1

        min_op = op
        while j < len(blocks):

            op += 1 if blocks[j] == 'W' else 0
            op -= 1 if blocks[i] == 'W' else 0

            i += 1
            j += 1

            min_op = min(min_op, op)

        return min_op

        