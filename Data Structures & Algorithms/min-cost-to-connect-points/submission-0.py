from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        minh = [(0, tuple(points[0]))] # (w, (x, y))
        res = 0
        visited = set() # (x, y)

        while len(visited) != len(points):
            w, coord = heappop(minh)

            if coord in visited:
                continue
            
            visited.add(coord)
            res += w

            xi, yi = coord
            
            for xj, yj in points:
                heappush(minh, (abs(xi - xj) + abs(yi - yj), (xj, yj)))
        
        return res