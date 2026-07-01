class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ysize, xsize = m, n

        grid = [ [1] * xsize  for y in range(ysize) ]

        for y in range(1, ysize):

            for x in range(1, xsize):
                grid[y][x] = grid[y - 1][x] + grid[y][x - 1]

        return grid[-1][-1] 