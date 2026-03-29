class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ysize, xsize = len(grid), len(grid[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        res = 0

        def dfs(y, x):
            if not (0 <= y < ysize) or not (0 <= x < xsize) or grid[y][x] == 0:
                return 0
            
            grid[y][x] = 0
            temp = 1
            for yd, xd in dirs:
                temp += dfs(y + yd, x + xd)
            
            return temp
            

        for y in range(ysize):
            for x in range(xsize):                
                res = max(res, dfs(y, x))
        
        return res

