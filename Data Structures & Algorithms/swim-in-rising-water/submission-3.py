from heapq import heappop, heappush

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        size = len(grid)
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        
        minh = [(grid[0][0], 0, 0)] # elev, y, x
        lvl = 0
        visited = set()

        while minh:
            elev, y, x = heappop(minh)

            if (y, x) in visited:
                continue
            
            visited.add((y, x))

            lvl = max(lvl, elev)

            if (y, x) == (size - 1, size - 1):
                break
            
            for yd, xd in dirs:
                if 0 <= (ny := y + yd) < size and 0 <= (nx := x + xd) < size:
                    heappush(minh, (grid[ny][nx], ny, nx))
        
        return lvl
