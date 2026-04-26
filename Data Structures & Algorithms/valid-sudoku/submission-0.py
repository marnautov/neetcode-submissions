class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r, row in enumerate(board):
            for c, val in enumerate(row):
                sq = c//3 + (r//3) * 3
                if val == '.':
                    continue
                if val in rows[r] or val in cols[c] or val in squares[sq]:
                    return False		
                rows[r].add(val)
                cols[c].add(val)
                squares[sq].add(val)
        return True
                