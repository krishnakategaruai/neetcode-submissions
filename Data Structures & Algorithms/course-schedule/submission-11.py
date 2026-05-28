class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses >1000 or numCourses<0 :
            return False
        if len(prerequisites) > 1000 :
            return False

        adj_list = {i:[] for i in range(numCourses)}
        for course,pre in prerequisites:
            adj_list[course].append(pre)
        
        

        def dfs(looking_key,key,visited):
            if key not in visited:
                visited.append(key)
            
                if key in adj_list :
                    for value in adj_list[key]:
                        if value == looking_key:
                            return False
                        if not dfs(looking_key,value,visited):
                            return False
            
            return True
            
            
            
        
        for course,pre in prerequisites:
            visited = []
            if not dfs(course,course,visited):
                return False
        return True

        