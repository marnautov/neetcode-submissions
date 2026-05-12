class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()   

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            k = ord(ch) - ord('a')
            if not node.children[k]:
                node.children[k] = TrieNode()
            node = node.children[k]

        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root

        for ch in word:
            k = ord(ch) - ord('a')
            if not node.children[k]:
                return False
            node = node.children[k]

        return node.is_end
       
    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for ch in prefix:
            k = ord(ch) - ord('a')
            if not node.children[k]:
                return False
            node = node.children[k]
            
        return True  