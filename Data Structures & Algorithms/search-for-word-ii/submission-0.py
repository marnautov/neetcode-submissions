class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        results = []

        root = TrieNode()
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.word = word
            
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, node):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return

            if (r,c) in seen:
                return
            
            ch = board[r][c]

            if ch not in node.children:
                return

            seen.add((r,c))

            node = node.children[ch]

            if node.word:
                results.append(node.word)
                node.word = None

            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            seen.remove((r,c))
                

        for i, row in enumerate(board):
            for j, _ in enumerate(row):
                seen = set()
                dfs(i, j, root)

        return results

        