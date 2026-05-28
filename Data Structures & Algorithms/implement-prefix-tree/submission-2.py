class PrefixTree:
    class Node:
        def __init__(self):
            self.children = {}
            self.end = False

    def __init__(self):
        self.root = self.Node()
    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = self.Node()
            current = current.children[ch]
        current.end = True
    def search(self, word: str) -> bool:
        current = self.root
        for ch in word:
            if ch in current.children:
                    current = current.children[ch]
                    if current.end:
                        return True
            else:
                return False
        return False   

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for ch in prefix:
            if ch in current.children:
                current = current.children[ch]
            else:
                return False
        
        return True
        
        