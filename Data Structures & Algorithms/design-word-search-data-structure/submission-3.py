class TrieNode:

    def __init__(self) -> None:
        self.children: dict[str, 'TrieNode'] = {}
        self.is_end: bool = False


class WordDictionary:

    def __init__(self) -> None:
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        

    def search(self, word: str) -> bool:

        def dfs(pos: int, node: 'TrieNode') -> bool:
            for i in range(pos, len(word)):
                ch = word[i]

                if ch == '.':
                    return any(
                        dfs(i + 1, child) 
                        for child in node.children.values()
                    )
                        
                if ch not in node.children:
                    return False

                node = node.children[ch]

            return node.is_end

        return dfs(0, self.root)
        
