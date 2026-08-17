class TreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] is None:
                cur.children[i] = TreeNode()
            cur = cur.children[i]
        cur.isEndOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] is not None:
                cur = cur.children[i]
                continue
            else:
                return False
        return cur.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if cur.children[i] is not None:
                cur = cur.children[i]
                continue
            else:
                return False
        return True        
        