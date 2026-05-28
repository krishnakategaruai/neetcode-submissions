class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        neg_diag_set = set()
        pos_diag_set = set()
        col_hash = set()

        boards = [["."] * n for _ in range(n)]
        res = []
        def backtrack(r):
            
            if r == n:
                rows = ["".join(row) for row in boards]
                res.append(rows)
                return 
            for col in range(n):

                #diagnol checks
                neg_diag = r-col
                pos_diag = r+col

                if col in col_hash or neg_diag in neg_diag_set or pos_diag in pos_diag_set:
                    continue

                col_hash.add(col)
                neg_diag_set.add(neg_diag)
                pos_diag_set.add(pos_diag)
                boards[r][col] = "Q"

                #add
                backtrack(r+1)

                #sub
                col_hash.remove(col)
                neg_diag_set.remove(neg_diag)
                pos_diag_set.remove(pos_diag)

                boards[r][col] = "."
        backtrack(0)
        return res
