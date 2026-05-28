class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #TRAVERSE FROM SIDES
        #FIND OUT ALL THE R,C WHICH ARE CONNECTED TO THEM 
        #APART FROM THAT MARK EVERY ITEM TO X

        rows = len(board)
        cols = len(board[0])
        from collections import deque
        oset = deque()
        set_of_o = []

        #Load into oset all corners that are O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r == 0 or r == rows-1 or c == 0  or c == cols-1):
                    oset.append((r,c))
                    set_of_o.append([r,c])
        
        #multi bfs using loaded oset
        while oset:
            (r,c) = oset.popleft()
            for d in [[-1,0],[1,0],[0,-1],[0,1]]:
                nr = r + d[0]
                nc = c + d[-1]
                if nr<0 or nc<0 or nr>=rows  or nc >= cols:
                    continue
                #loading adjacent O which are connected to corners:
                if board[nr][nc] != "O" or [nr,nc] in set_of_o:
                    continue
                oset.append((nr,nc))
                set_of_o.append([nr,nc])
        
        for r in range(rows):
            for c in range(cols):
                if [r,c] not in set_of_o and board[r][c] == "O":
                    board[r][c] = "X"

        return 







        



