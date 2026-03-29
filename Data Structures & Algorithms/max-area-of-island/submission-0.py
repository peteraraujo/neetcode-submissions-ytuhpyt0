class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ySize, xSize = len(grid), len(grid[0])

        res = 0
        visited = set()

        def dfs(y, x):

            if y < 0 or x < 0 or y >= ySize or x >= xSize or grid[y][x] == 0 or (y, x) in visited:
                return 0

            visited.add((y, x))
        
            return 1 + (
                dfs(y, x + 1) +
                dfs(y, x - 1) +
                dfs(y + 1, x) +
                dfs(y - 1, x)
            )

        
        for y in range(ySize):
            for x in range(xSize):
                if grid[y][x] != 0 and (y, x) not in visited:
                    res = max(res, dfs(y, x))
        
        return res
