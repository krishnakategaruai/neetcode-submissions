class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row
        #col
        #0-3 #0- 3
        from collections import defaultdict
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):

                val = board[i][j]

                if val == ".":
                    continue
                
                if val in row[i] or val in col[j] or val in square[(i//3,j//3)]:
                    return False
                
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                square[(i//3,j//3)].add(board[i][j])
            
        return True

                