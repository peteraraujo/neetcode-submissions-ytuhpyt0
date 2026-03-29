class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ysize, xsize = len(grid), len(grid[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        res = 0

        temp = 0

        def dfs(y, x):
            nonlocal temp
            if not (0 <= y < ysize) or not (0 <= x < xsize) or grid[y][x] == 0:
                return
            
            temp += 1
            grid[y][x] = 0

            for yd, xd in dirs:
                dfs(y + yd, x + xd)




        for y in range(ysize):
            for x in range(xsize):
                temp = 0
                dfs(y, x)
                res = max(res, temp)
        
        return res

