from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        started = set()

        for a, b in prerequisites:
            adj[a].append(b)
        
        def dfs(course, visited):
            if course in visited:
                return False
            
            if course in started:
                return True

            started.add(course)
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

