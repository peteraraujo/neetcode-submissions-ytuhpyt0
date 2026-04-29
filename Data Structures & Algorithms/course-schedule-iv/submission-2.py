from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)
        
        nodeToPre = defaultdict(set)

        def dfs(node):
            if node in nodeToPre:
                return
            
            nodeToPre[node]
            
            for nei in adj[node]:
                dfs(nei)
                nodeToPre[node].add(nei)
                nodeToPre[node].update(nodeToPre[nei])
        
        for node in range(numCourses):
            dfs(node)

        return [ p in nodeToPre[c] for p, c in queries ]
            




