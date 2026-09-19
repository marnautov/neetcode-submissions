class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def find_word(r, c, i):
            if r < 0 or r >= len(board):
                return False

            if c < 0 or c >= len(board[0]):
                return False

            if board[r][c] != word[i]:
                return False

            i += 1

            if i == len(word):
                return True

            char = board[r][c]
            board[r][c] = '-'

            found = (
                find_word(r + 1, c, i)
                or find_word(r - 1, c, i)
                or find_word(r, c + 1, i)
                or find_word(r, c - 1, i)
                )

            board[r][c] = char

            return found


        for r, row in enumerate(board):
            for c, char in enumerate(row):
                if find_word(r, c, 0):
                    return True

        return False
