class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #base conditions
        rows = len(grid)
        cols = len(grid[0])

        if rows<0 or cols<0 or rows>100 or cols>100:
            return 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]!='1' and grid[i][j]!='0':
                    return 0
            
        
        #map reached
        #move towards unmapped until it is broken

        output = 0
        #up #down #bottom #down 

        def dfs(r,c):
             # bounds
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            if grid[r][c]=='#' or grid[r][c] == '0':
                return

            grid[r][c] = '#'

            dfs(r+1,c)

            dfs(r-1,c)

            dfs(r,c+1)

            dfs(r,c-1)

            
            return 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i,j)
                    output = output + 1

        return output
            


            

