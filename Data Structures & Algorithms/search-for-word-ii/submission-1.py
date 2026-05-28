class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = "#"

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = Trie()
        result = set()
        rows = len(board)
        cols = len(board[0])
        #loading all the characters of words
        for word in words:
            current = root
            for letter in word:
                if letter not in current.children:
                    current.children[letter] = Trie()
                    
                current = current.children[letter]

            current.is_word = True
            current.word = word
        


        #loaded all the charcters of words

        #now going throught all the letters dfs way
        
        def dfs(r,c,node):

            if r<0 or c<0  or r>= len(board) or c>= len(board[0]):
                return None



            ch = board[r][c]
            
 

            if ch == "#" or ch not in node.children:
                return
            
            next_node = node.children[ch]

        
            if next_node.is_word:
                result.add(next_node.word)

            board[r][c] = '#'
            dfs(r+1,c,next_node)

            dfs(r-1,c,next_node)

            dfs(r,c+1,next_node)

            dfs(r, c-1,next_node)

            board[r][c] = ch

            return 

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return list(result)
