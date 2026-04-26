from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        
        adj = defaultdict(list)

        for f, t, w in edges:
            adj[f].append((t, w))


        mh = [(0, src)]
        visited = set()

        res = {vtx : -1 for vtx in range(n)}

        while mh:
            dist, node = heappop(mh)   

            if res[node] != -1:
                continue

            res[node] = dist        
            
            for nei, w in adj[node]:
                heappush(mh, (dist + w, nei))
            
            visited.add(node)
        
        return res

            


