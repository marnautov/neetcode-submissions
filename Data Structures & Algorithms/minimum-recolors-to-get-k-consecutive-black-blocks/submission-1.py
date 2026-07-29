class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        op = blocks[:k].count('W')
        min_op = op

        i, j = 0, k
        while j < len(blocks):
            op += blocks[j] == 'W'
            op -= blocks[i] == 'W'
            min_op = min(min_op, op)

            i += 1
            j += 1

        return min_op

            
        