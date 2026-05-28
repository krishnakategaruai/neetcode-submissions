class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_ = {i : [] for i in range(n)}
        for en1,en2 in edges:
            adj_[en1].append(en2)
            adj_[en2].append(en1)
        is_visited = set()
        con_comps = []

        def dfs(node):

            if node not in is_visited:
                is_visited.add(node)
                result.append(node)
                if len(adj_[node])>=1:
                    for value in adj_[node]:
                        dfs(value)            
            return 
            
            
                
            
        

        for i in range(n):
            result = []
            dfs(i)
            if len(result)>0:
                con_comps.append(result)

        count = len(con_comps)
        return count
        