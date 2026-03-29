class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        
        
        # adj: 
        # Node -> [(nei, index of edge)]
        # 1 -> [(2, 0)]
        adj = {i:[] for i in range(1, len(edges) + 1) }

        

        for index, edge in enumerate(edges):
            adj[edge[0]].append((edge[1], index))
            adj[edge[1]].append((edge[0], index))

        visited = set()
        maxLoopyEdgeIndex = -1

        print(adj)
    
        # Returns True if is loop. False otherwise.
        def dfs(current, pre):

            isInLoop = False
            visited.add(current)

            for nei, edgeIndex in adj[current]:
                if nei == pre:
                    continue
                
                if nei in visited or dfs(nei, current):
                    nonlocal maxLoopyEdgeIndex
                    maxLoopyEdgeIndex = max(maxLoopyEdgeIndex, edgeIndex)
                    isInLoop = not isInLoop
                    
            
            return isInLoop
        
        dfs(1, -1)
        return edges[maxLoopyEdgeIndex]

                    
                


                



        
