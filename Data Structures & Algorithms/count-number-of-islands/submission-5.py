class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        sizey, sizex = len(grid), len(grid[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        res = 0

        def dfs(y, x):
            if not (0 <= y < sizey) or not (0 <= x < sizex) or grid[y][x] == '0':
                return
            
            grid[y][x] = '0'

            for yd, xd in dirs:
                dfs(y + yd, x + xd)
            
        for y in range(sizey):
            for x in range(sizex):
                if grid[y][x] == '1':
                    res += 1
                    dfs(y, x)
        
        return res
