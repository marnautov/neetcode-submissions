class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, 'TrieNode'] = {}
        self.word: str | None = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        def dfs(r: int, c: int, node: TrieNode) -> None:
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            ch = board[r][c]
            if ch not in node.children:
                return
            node = node.children[ch]
            if node.word:
                res.append(node.word)
                node.word = None

            board[r][c] = '#'

            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            board[r][c] = ch

        rows = len(board)
        cols = len(board[0])
        res = []

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res
        