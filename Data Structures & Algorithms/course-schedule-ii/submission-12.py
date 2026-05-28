class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses<0 or numCourses>1000:
            return False
        
        adj_ = {i:[] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            adj_[pre].append(course)
        result = []
        visited = set()
        path = set()
        
         
        #lookup is prereq of pre
        def dfs(pre):
            if pre in path:
                return False
            path.add(pre)
            if pre not in result:
                
                for course in adj_[pre]:
                    if not dfs(course):
                        return False
            path.remove(pre)
            # visited.add(pre)
            result.append(pre)
            return True
        
        for course,pre in prerequisites:
            if not dfs(pre):
                return []
        #adding remaining :
        result = result[::-1]
        for i in range(numCourses):
            
            if i in result:
                continue
            result.append(i)
        return result
            

                
                    
        
