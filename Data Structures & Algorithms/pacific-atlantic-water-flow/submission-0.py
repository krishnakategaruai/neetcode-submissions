class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])

        if rows < 0 or cols < 0  or rows > 100 or cols > 100:
            return []

        pacific = set()
        atlantic = set()

        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        def dfs(r,c,visit):
            
            if (r,c) in visit:
                    return
            visit.add((r,c))

            for d in directions:
                nr = r + d[0]
                nc = c + d[1]

                if nr>=rows or nc >= cols or nr < 0  or nc < 0 :
                    continue

                if heights[nr][nc]<heights[r][c]:
                    continue
                
               

                
                dfs(nr,nc,visit)

        #pacific
        
        for c in range(cols):
            dfs(0,c,pacific)
            dfs(rows-1, c, atlantic)
        
        for r in range(rows):

            dfs(r,0, pacific)
            dfs(r,cols-1,atlantic)

        
        return [ list(x) for x in pacific.intersection(atlantic)]

                


                


            