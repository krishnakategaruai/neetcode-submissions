class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        if rows<1 or cols<1 or rows>50 or cols>50:
            return 0
        
        def dfs(r,c):

            if r<0 or c<0 or r>=rows or c >=cols:
                return 0
            if grid[r][c] == "#" or grid[r][c]== 0:
                return 0
            
            grid[r][c] = "#"
            
            area = 1

            area = area + dfs(r+1,c)

            area = area + dfs(r-1,c)

            area = area + dfs(r,c+1)

            area = area + dfs(r,c-1)

            return area
        result = [0]
        for i in range(rows):
            
            for j in range(cols):
                
                if grid[i][j]==1:
                    output = dfs(i,j)
                    result.append(output)
                    print(result)
                

        
        return max(result)

        