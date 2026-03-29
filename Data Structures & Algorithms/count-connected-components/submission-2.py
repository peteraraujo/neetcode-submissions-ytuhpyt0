class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # Adjacent map
        adj = [ [] for i in range(n) ]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        count = 0

        def dfs(current, pre):

            if current in visited:
                return

            visited.add(current)

            for nei in adj[current]:
                if nei != pre:
                    dfs(nei, current)
            
        
        for node in range(n):
            if node not in visited:
                dfs(node, -1)
                count += 1
        
        return count
        
