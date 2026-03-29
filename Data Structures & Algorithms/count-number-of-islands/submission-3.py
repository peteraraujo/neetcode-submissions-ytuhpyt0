class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ysize, xsize = len(grid), len(grid[0])
        res = 0

        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(y, x):
            if not (0 <= y < ysize) or not (0 <= x < xsize) or grid[y][x] == "0":
                return
            
            grid[y][x] = "0"

            for yd, xd in dirs:
                dfs(y + yd, x + xd)
        
        for y in range(ysize):
            for x in range(xsize):
                if grid[y][x] == "1":
                    res += 1
                    dfs(y, x)
        return res