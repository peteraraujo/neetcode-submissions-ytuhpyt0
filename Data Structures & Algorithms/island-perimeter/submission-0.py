class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ysize, xsize = len(grid), len(grid[0])

        visited = set()
        res = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))


        def dfs(y, x):
            nonlocal res

            if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]) or grid[y][x] == 0:
                res += 1
                return
            
            if (y, x) in visited:
                return
            
            visited.add((y, x))
            
            for d in directions:
                dfs(y + d[0], x + d[1])

        for y in range(ysize):
            for x in range(xsize):
                if grid[y][x] == 1:
                    dfs(y, x)
                    return res
        
        return res