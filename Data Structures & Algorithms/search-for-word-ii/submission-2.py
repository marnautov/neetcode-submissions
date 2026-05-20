class TrieNode:
    def __init__(self) -> None:
        self.children: list["TrieNode | None"] = [None] * 26
        self.word: str | None = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []

        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                idx = ord(ch) - ord('a')
                if node.children[idx] is None:
                    node.children[idx] = TrieNode()
                node = node.children[idx]
            node.word = word

        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int, node: TrieNode) -> None:
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            ch = board[r][c]
            if ch == '#':
                return
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                return
            node = node.children[idx]

            if node.word:
                res.append(node.word)
                node.word = None

            board[r][c] = '#'

            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            board[r][c] = ch


        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res

