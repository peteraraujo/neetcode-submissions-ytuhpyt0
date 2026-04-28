from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b, w in edges:
            adj[a].append((b, w))
            adj[b].append((a, w))
        
        minh = [] # (weight, nodeA, nodeB)
        for nei, w in adj[1]:
            heappush(minh, (w, 1, nei))
        
        visited = set([1])
        res = 0

        while len(visited) != n:
            if not minh:
                return -1
            w, a, b = heappop(minh)
            if b in visited:
                continue
            visited.add(b)
            res += w

            for nei, w in adj[b]:
                heappush(minh, (w, b, nei))
        
        return res