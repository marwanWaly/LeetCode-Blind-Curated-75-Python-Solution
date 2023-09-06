class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_graph = {c:[] for c in range(numCourses)}
        for c, pre in prerequisites:
            pre_graph[c].append(pre)
        
        visited = set()
        def dfs(c):
            if c in visited: # Loop detected
                return False
            
            if pre_graph[c] == []: # There are no prerequisites
                return True
            
            visited.add(c)
            for pre in pre_graph[c]:
                if not dfs(pre):
                    return False
            visited.remove(c)

            pre_graph[c] = [] # No need to re check again
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
