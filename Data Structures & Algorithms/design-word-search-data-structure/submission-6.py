class WordDictionary:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_end = False

    def __init__(self):
        self.root = self.Node()
        

    def addWord(self, word: str) -> None:
        current = self.root
        for ch in word :
            if ch not in current.children:
                current.children[ch] = self.Node()
            current = current.children[ch]
        current.is_end = True

        

    def search(self, word: str) -> bool:
        def solve(node,i):
            if i == len(word):
                return node.is_end
            letter = word[i]
            if letter == ".":
                for ch in node.children.values():
                    if solve(ch,i+1):
                        return True
            else:
                if letter not in node.children:
                    return False
                return solve(node.children[letter],i+1)
            return False
        return solve(self.root,0)


        
