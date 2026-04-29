from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[a].append(b)
        
        added = set() # Global
        res = []

        # Returns:
        # - False: If there is a cycle
        # - True: If no cycle was detected
        def dfs(node, visited):
            if node in visited:
                return False
            
            if node in added:
                return True
            
            visited.add(node)
            added.add(node)

            for nei in adj[node]:
                if not dfs(nei, visited):
                    return False # Propagation if cycle flag
            
            res.append(node)
            visited.remove(node)

            return True
        
        for node in range(numCourses):
            if not dfs(node, set()):
                return []
        
        return res


        
