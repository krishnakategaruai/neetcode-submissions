class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #e = n -1
        if len(edges) != n -1 and len(edges) <= (n*(n-1)/2):
            return False
        adj_ = {i:[] for i in range(n)}
        is_visited = set()
        for en1,en2 in edges:
            adj_[en1].append(en2)
            adj_[en2].append(en1)

        def dfs(node,parent):

            if node in is_visited:
                return False
            if node not in is_visited:
                is_visited.add(node)
                for value in adj_[node]:
                    if value == parent:
                        continue
                    if not dfs(value,node):
                        return False
            
            return True     


        if not dfs(0,-1):
            return False     
        return len(is_visited) == n