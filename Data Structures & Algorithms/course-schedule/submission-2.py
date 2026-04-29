from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[a].append(b)
        
        def dfs(course, visited):
            if course in visited:
                return False
            
            visited.add(course)

            for nei in adj[course]:
                if not dfs(nei, visited):
                    return False
            
            visited.remove(course)
            
            return True
            
        for start in range(numCourses):
            if not dfs(start, set()):
                return False
        
        return True

