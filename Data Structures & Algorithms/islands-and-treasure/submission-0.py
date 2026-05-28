from collections import deque
class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        if not grid:
            return
        
        items = deque()
        
    
        rows = len(grid)
        cols = len(grid[0])

        if rows<0 or cols < 0  or rows>100 or cols > 100:
            return
        
        #validating grid:
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]!= 0 and grid[r][c]!= -1 and grid[r][c]!= 2147483647:
                    return
                if grid[r][c] == 0:
                    items.append((r,c))
        
        while items:
            r,c = items.popleft()
            for d1,d2 in  [[1,0], [-1,0], [0,1], [0,-1]] :
                nr , nc = r+d1,c+d2
                # boundary check
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                if grid[nr][nc]!= 2147483647:
                    continue
                
                grid[nr][nc] = grid[r][c]+1

                items.append((nr,nc))


            



        
        
        
        

         

            
        

