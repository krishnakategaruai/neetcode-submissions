class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rotten_fruits = deque()
        rows = len(grid)
        cols = len(grid[0])
        count = -1 

        if rows == 1 and cols == 1 and grid[0][0]!=1:
            return 0

        #finding first rotten fruit
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten_fruits.append((r,c))
        #got all rotten fruits

        #BFS Levels to make sure all are rotten
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        while rotten_fruits:
            count+=1
            for _ in range(len(rotten_fruits)):
                r,c = rotten_fruits.popleft()
                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]

                    if nr <0 or nc < 0  or nr >= rows or nc >= cols:
                        continue

                    if grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue
                    
                    rotten_fruits.append((nr,nc))
                    grid[nr][nc] =2
                
            
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return max(count,0)




        
        