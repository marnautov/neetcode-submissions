class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r, row in enumerate(board):
            for c, value in enumerate(row):

                if value == '.':
                    continue

                sq = c // 3 + r // 3 * 3

                if value in rows[r]:
                    return False
                if value in cols[c]:
                    return False
                if value in squares[sq]:
                    return False

                rows[r].add(value)
                cols[c].add(value)
                squares[sq].add(value)

        return True
                
        