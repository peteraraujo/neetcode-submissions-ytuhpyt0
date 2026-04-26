from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for o, d, w in times:
            adj[o].append((d, w))
        
        minh = [(0, k)]

        maxx = 0
        visited = set()

        while minh:
            dist, node = heappop(minh)
            if node in visited:
                continue
            
            visited.add(node)
            maxx = max(maxx, dist)

            for nei, wei in adj[node]:
                heappush(minh, (wei + dist, nei))
        
        return -1 if len(visited) != n else maxx



