class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ysize, xsize = len(grid), len(grid[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        res = 0

        for y in range(ysize):
            for x in range(xsize):
                if grid[y][x] == 0:
                    continue
                for d in dirs:
                    yd = y + d[0]
                    xd = x + d[1]
                    if yd < 0 or yd >= ysize or xd < 0 or xd >= xsize or grid[yd][xd] == 0:
                        res += 1
        
        return res
                




