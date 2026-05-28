class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        adj_ = {i:[] for i in range(1,len(edges)+1)}
        for [en1,en2] in edges:
            adj_[en1].append(en2)
            adj_[en2].append(en1)

        result = set()
        visited = set()
        def dfs(node,parent):
            if node in visited:
                return 

            visited.add(node)
            result.add(node)
            if len(adj_[node])>1 or (len(adj_[node]) == 1 and adj_[node][0]!= parent):
                for value in adj_[node]:
                    if value == parent:
                        continue
                    dfs(value,node)

            count = 0

            for value in adj_[node]:

                if value in result:
                    count += 1

            if count < 2:
                result.remove(node)
            return 
            

        dfs(edges[0][0],-1)
        for [en1,en2] in edges[::-1]:
            if en1 in result and en2 in result:
                return [en1,en2]
        
        return []

        